# Writing a challenge spec

A *challenge spec* is a YAML file that describes a single challenge so the CLI can
push it to a remote GZ::CTF server with `gz game push-challenge`. The file must be
named `challenge.yml` (or `challenge.yaml`) and live in the challenge directory:

```sh
gz game push-challenge --game-id [game id] [challenge_directory]
```

`push-challenge` looks for `challenge.yml` first, then falls back to
`challenge.yaml`, in the directory you point it at.

```
my-challenge/
├── challenge.yml      # the spec described on this page
├── attachment.zip     # files referenced from the spec
└── ...
```

## A minimal example

```yaml
title: "Baby RSA"
category: Crypto
description: "Can you break this textbook RSA?"
author: alice

deployment:
  deploymentType: StaticAttachment
  attachment:
    - type: Local
      path: attachment.zip

flag:
  - "flag{t3xtb00k_rs4_15_br0k3n}"

scoring:
  difficulty: 1.0
  base_points: 500
  min_score_ratio: 0.2
  bloodBonus: true
```

## Top-level fields

| Field           | Type                       | Required | Default | Notes |
|-----------------|----------------------------|:--------:|---------|-------|
| `title`         | string                     | yes      | —       | Challenge name, at least 1 character. |
| `category`      | [category](#categories)    | yes      | —       | One of the challenge categories. |
| `deployment`    | [deployment](#deployment)  | yes      | —       | How the challenge is delivered. |
| `flag`          | list of strings            | yes      | —       | Accepted flags (see [flags](#flags)). |
| `scoring`       | [scoring](#scoring)        | yes      | —       | Point and difficulty configuration. |
| `description`   | string                     | no       | —       | Markdown body shown to players, up to 8192 characters. |
| `author`        | string                     | no       | —       | Challenge author, for your own bookkeeping. |
| `hints`         | list of strings            | no       | —       | Hints displayed to players. |
| `maxAttempts`   | integer                    | no       | unlimited | Maximum number of flag submissions per team. |
| `hidden`        | boolean                    | no       | `false` | When `false`, the challenge is enabled (made visible) after it is pushed. Set to `true` to keep it hidden. |
| `prerequisites` | list                       | no       | —       | Reserved for future use. |

## deployment

Describes how the challenge is delivered to players.

| Field            | Type                              | Required | Default | Notes |
|------------------|-----------------------------------|:--------:|---------|-------|
| `deploymentType` | [challenge type](#challenge-types) | yes     | —       | The kind of challenge. |
| `attachment`     | list of [attachment](#attachment) | no       | —       | Files handed to players (attachment challenges). |
| `containers`     | [containers](#containers)         | no       | —       | Container image configuration (container challenges). |
| `scripts`        | object                            | no       | —       | Reserved for future build-script support. |

### attachment

| Field  | Type   | Required | Notes |
|--------|--------|:--------:|-------|
| `type` | string | yes      | `Local` for a file in the challenge directory, `Remote` for a URL. |
| `path` | string | yes      | For `Local`, the file path relative to the challenge directory. For `Remote`, the download URL. |

### containers

| Field                    | Type    | Required | Default  | Notes |
|--------------------------|---------|:--------:|----------|-------|
| `image`                  | string  | yes      | —        | Container image reference. |
| `servicePort`            | integer | yes      | —        | Port the service listens on, `1`–`65535`. |
| `networkMode`            | string  | no       | `Open`   | One of [network modes](#network-modes). |
| `enable_traffic_capture` | boolean | no       | —        | Capture challenge traffic for review. |
| `limits`                 | object  | no       | —        | Per-instance resource limits: `cpu`, `memory`, `storage`. |

## scoring

| Field             | Type    | Required | Default | Notes |
|-------------------|---------|:--------:|---------|-------|
| `difficulty`      | float   | no       | `1.0`   | Score decay difficulty, `> 0` and `<= 5`. Higher means the score drops faster as more teams solve it. |
| `base_points`     | integer | no       | `500`   | The starting (maximum) score, `> 0`. |
| `min_score_ratio` | float   | no       | `0.2`   | The floor the score can decay to, as a fraction of `base_points`, between `0` and `1`. |
| `bloodBonus`      | boolean | no       | `true`  | Whether first/second/third-blood bonuses apply to this challenge. |

## flags

`flag` is a list of accepted flag strings. Each flag is at most 127 characters.

- **Static attachment** challenges accept the literal flags you list here.
- **Container** challenges currently push these flags as static flags as well.

## Challenge types

`deployment.deploymentType` must be one of:

| Value               | Meaning |
|---------------------|---------|
| `StaticAttachment`  | A downloadable attachment with fixed flags. |
| `StaticContainer`   | A shared container with fixed flags. |
| `DynamicAttachment` | Per-team attachments (not yet supported by `push-challenge`). |
| `DynamicContainer`  | Per-team containers with dynamic flags (not yet supported by `push-challenge`). |

> **Note:** `push-challenge` does not yet support the dynamic challenge types;
> pushing a `Dynamic*` challenge currently raises an error.

## Categories

`category` must be one of:

`Misc`, `Crypto`, `Pwn`, `Web`, `Reverse`, `Blockchain`, `Forensics`,
`Hardware`, `Mobile`, `PPC`, `AI`, `Pentest`, `OSINT`.

Run `gz list-challenge-categories` to print this list, and
`gz list-challenge-types` for the challenge types.

## Network modes

`deployment.containers.networkMode` must be one of:

| Value      | Meaning |
|------------|---------|
| `Open`     | The container can reach the internet (default). |
| `Isolated` | The container is isolated from external networks. |
| `Custom`   | A custom network policy configured on the server. |

## A container example

```yaml
title: "Notes"
category: Web
description: "A note-taking app with a twist."
author: bob

deployment:
  deploymentType: StaticContainer
  containers:
    image: registry.example.com/notes:latest
    servicePort: 80
    networkMode: Open
    enable_traffic_capture: false

flag:
  - "flag{st0r3d_x55_15_fun}"

scoring:
  difficulty: 2.0
  base_points: 1000
  min_score_ratio: 0.25
  bloodBonus: true

hints:
  - "The flag is in the admin's cookies."
maxAttempts: 0
hidden: false
```
