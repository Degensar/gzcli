import click
import requests
from click.shell_completion import get_completion_class
from gzcli.cli.errors import error_wrap
from gzcli.cli.auth import (
    _save_edited_profiles,
    _load_profiles,
    require_existing_profile,
)
from gzcli.cli.config import PROFILES_PATH
from gzcli.api._http import APIProfile, make_post
from gzcli.api.models.enum import ChallengeCategory, ChallengeType


@click.group()
@click.version_option("0.1.0")
def gz():
    pass


@gz.command()
@click.option("--url", prompt=True, required=True)
@click.option("--username", prompt=True, required=True)
@click.option("--password", prompt=True, required=True, hide_input=True)
@click.option("--challenge")
@click.option("--profile", default="default", required=True)
@error_wrap
def login(
    url: str,
    username: str,
    password: str,
    challenge: str | None = None,
    profile: str = "default",
):

    login_endpoint = f"{url.strip('/')}/api/account/login"
    r = requests.post(
        login_endpoint,
        headers={"Content-Type": "application/json"},
        json={"challenge": challenge, "userName": username, "password": password},
    )
    if r.status_code == 401:
        raise click.ClickException("401 incorrect login credentials")
    elif r.status_code == 404:
        raise click.ClickException(f"404 {login_endpoint} not found")

    token = r.cookies["GZCTF_Token"]
    all_profiles = _load_profiles(PROFILES_PATH)
    all_profiles[profile] = {"url": url, "username": username, "token": token}
    _save_edited_profiles(all_profiles, PROFILES_PATH)
    click.echo(f"login successful, stored login credentials for profile {profile}")


@gz.command()
@require_existing_profile
@error_wrap
def logout(profile: APIProfile):
    make_post(profile, "/api/account/logout")
    all_profiles = _load_profiles(PROFILES_PATH)
    all_profiles.pop(profile.name)
    _save_edited_profiles(all_profiles, PROFILES_PATH)
    click.echo(f"profile {profile.name} logged out successfully")


@gz.command("list-challenge-categories")
def list_challenge_categories():
    categories = ChallengeCategory.__args__
    click.echo("\n".join(f"{i:2}. {j}" for i, j in enumerate(categories, start=1)))


@gz.command("list-challenge-types")
def list_challenge_types():
    challenge_types = ChallengeType.__args__
    click.echo("\n".join(f"{i:2}. {j}" for i, j in enumerate(challenge_types, start=1)))
    click.echo(
        "for more information visit https://gzctf.gzti.me/guide/start/introduction"
    )


@gz.command()
@click.argument("shell", type=click.Choice(["bash", "zsh", "fish"]))
def completion(shell: str):
    """\b
    print the shell completion script for the given shell.
    enable it by sourcing the output, for example:
        gz completion bash >> ~/.bashrc      # bash
        gz completion zsh  >> ~/.zshrc        # zsh
        gz completion fish >  ~/.config/fish/completions/gz.fish
    then restart your shell.
    """
    completion_cls = get_completion_class(shell)
    if completion_cls is None:
        raise click.ClickException(f"shell completion is not supported for {shell}")
    # `gz` is fully wired with its subcommands by the entrypoint before this runs
    click.echo(completion_cls(gz, {}, "gz", "_GZ_COMPLETE").source())
