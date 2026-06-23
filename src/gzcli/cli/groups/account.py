"""Commands for managing user accounts on the remote ctf server"""

import click
import requests
from pydantic import ValidationError
from gzcli.cli.auth import _load_profiles, _save_edited_profiles
from gzcli.cli.config import PROFILES_PATH
from gzcli.cli.errors import error_wrap
from gzcli.api._http import APIProfile
from gzcli.api.account import register as register_account
from gzcli.api.models.account import RegisterModel


def _format_http_error(exc: requests.HTTPError) -> str:
    """turn an HTTP error from the server into a readable message"""
    resp = exc.response
    if resp is None:
        return str(exc)
    try:
        body = resp.json()
    except ValueError:
        body = None
    if isinstance(body, dict) and body.get("title"):
        return f"{resp.status_code} {body['title']}"
    return f"{resp.status_code} {resp.reason}"


@click.group()
def account():
    pass


@account.command()
@click.option("--url", prompt=True, required=True, help="the remote CTF server url")
@click.option(
    "-u",
    "--username",
    prompt=True,
    required=True,
    help="the account username, 3 to 15 characters",
)
@click.option(
    "-e", "--email", prompt=True, required=True, help="the account email address"
)
@click.option(
    "-p",
    "--password",
    prompt=True,
    required=True,
    hide_input=True,
    confirmation_prompt=True,
    help="the account password",
)
@click.option(
    "--challenge",
    default=None,
    help="captcha challenge token, if the server requires one",
)
@click.option(
    "--profile",
    default="default",
    help='the profile to store the session under if the server logs you in, "default" if unspecified',
)
@error_wrap
def register(
    url: str,
    username: str,
    email: str,
    password: str,
    challenge: str | None,
    profile: str,
):
    """\b
    register (create) a new user account on the remote CTF server.
    if the server activates accounts on registration you are logged in and the
    credentials are saved under the given profile; otherwise you must confirm
    your email or await admin approval before running `gz login`.
    """
    try:
        body = RegisterModel(
            userName=username, email=email, password=password, challenge=challenge
        )
    except ValidationError as exc:
        messages = "; ".join(err["msg"] for err in exc.errors())
        raise click.ClickException(f"invalid account information: {messages}")

    url = url.strip("/")
    api_profile = APIProfile(name=profile, url=url, token="", username=username)

    try:
        resp = register_account(api_profile, body)
    except requests.HTTPError as exc:
        raise click.ClickException(_format_http_error(exc))

    payload = resp.json() if resp.content else {}
    status = payload.get("data")

    if status == "LoggedIn":
        token = resp.cookies.get("GZCTF_Token", "")
        all_profiles = _load_profiles(PROFILES_PATH)
        all_profiles[profile] = {"url": url, "username": username, "token": token}
        _save_edited_profiles(all_profiles, PROFILES_PATH)
        click.echo(
            f"[+] account '{username}' registered and logged in, "
            f"credentials stored for profile {profile}"
        )
    elif status == "AdminConfirmationRequired":
        click.echo(
            f"[+] account '{username}' registered; "
            "an administrator must approve it before you can log in"
        )
    elif status == "EmailConfirmationRequired":
        click.echo(
            f"[+] account '{username}' registered; "
            "check your email to confirm the address before you can log in"
        )
    else:
        click.echo(payload.get("title") or f"[+] account '{username}' registered")
