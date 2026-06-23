# GZCTF CLI

A CLI built for interacting with [GZ::CTF](https://gzctf.gzti.me/) and its server API.

## Getting Started
### Since the tool is still in development phase, no built package is released yet.

### 1. Clone the repository
```sh
git clone https://github.com/Soltime5476/gzcli.git
```

### 2. Install the package into your python environment
The easiest way to do so is with [uv](https://github.com/astral-sh/uv) installed, simply run   
```sh
cd gzcli
uv sync
``` 
and uv will create a virtual environment with all dependencies installed.

## Example Usages

### login to GZ::CTF remote server
```sh
gz login --url [remote url] --username [username] --password [password]
```

### push a challenge to the remote server
```
gz game push-challenge --game-id [game_id] [challenge_directory]
```
this command requires a `challenge.yaml` (or `challenge.yml`) containing the challenge spec to be present in the challenge directory, see [writing a challenge spec](docs/challenge_spec.md) for documentation on the challenge spec format.

### register (create) a team on the remote server
```sh
gz team register --name [team name] --bio [optional team bio]
```
you must be logged in first (see `gz login`), and each user account can only own one team.

### register (create) an account on the remote server
```sh
gz account register --url [remote url] --username [username] --email [email]
```
you will be prompted for a password. if the server activates accounts on registration you are logged in immediately and the credentials are stored under `--profile`; otherwise confirm your email or await admin approval, then run `gz login`.

## Shell completion

`gz` ships with tab completion for bash, zsh and fish. Print the script for your shell and source it from your shell config:
```sh
gz completion bash >> ~/.bashrc       # bash
gz completion zsh  >> ~/.zshrc         # zsh
gz completion fish >  ~/.config/fish/completions/gz.fish
```
then restart your shell. To enable completion for the current session only:
```sh
eval "$(_GZ_COMPLETE=bash_source gz)"
```

## TODO List
- Complete all API endpoints and data models
- Fancy stuff (progress bars...)