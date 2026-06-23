import click
import requests
from gzcli.cli.errors import error_wrap
from gzcli.cli.auth import (
    _save_edited_profiles,
    _load_profiles,
    require_existing_profile,
)
from gzcli.cli.config import PROFILES_PATH
from gzcli.cli.output import success
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
    """\b
    log in to a remote CTF server and store the session for later commands.
    credentials are saved under the given profile (default: "default").
    """
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
    success(f"login successful, stored login credentials for profile {profile}")


@gz.command()
@require_existing_profile
@error_wrap
def logout(profile: APIProfile):
    """log out the given profile and remove its stored credentials."""
    make_post(profile, "/api/account/logout")
    all_profiles = _load_profiles(PROFILES_PATH)
    all_profiles.pop(profile.name)
    _save_edited_profiles(all_profiles, PROFILES_PATH)
    success(f"profile {profile.name} logged out successfully")


@gz.command("list-challenge-categories")
def list_challenge_categories():
    """list the challenge categories accepted in a challenge spec."""
    categories = ChallengeCategory.__args__
    click.echo("\n".join(f"{i:2}. {j}" for i, j in enumerate(categories, start=1)))


@gz.command("list-challenge-types")
def list_challenge_types():
    """list the challenge types accepted in a challenge spec."""
    challenge_types = ChallengeType.__args__
    click.echo("\n".join(f"{i:2}. {j}" for i, j in enumerate(challenge_types, start=1)))
    click.echo(
        "for more information visit https://gzctf.gzti.me/guide/start/introduction"
    )
