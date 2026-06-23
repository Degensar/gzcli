"""Commands for managing teams on the remote ctf server"""

import click
import requests
from pydantic import ValidationError
from gzcli.cli.auth import require_existing_profile, APIProfile
from gzcli.cli.errors import error_wrap
from gzcli.cli.output import success
from gzcli.api.team import create_team
from gzcli.api.models.info import TeamUpdateModel


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
def team():
    pass


@team.command()
@click.option("-n", "--name", required=True, help="the team name, at most 20 characters")
@click.option(
    "-b",
    "--bio",
    default=None,
    help="an optional team description, at most 72 characters",
)
@require_existing_profile
@error_wrap
def register(name: str, bio: str | None, profile: APIProfile):
    """\b
    register (create) a new team on the remote CTF server.
    each user account can only own one team.
    """
    try:
        body = TeamUpdateModel(name=name, bio=bio)
    except ValidationError as exc:
        messages = "; ".join(err["msg"] for err in exc.errors())
        raise click.ClickException(f"invalid team information: {messages}")

    try:
        created = create_team(profile, body)
    except requests.HTTPError as exc:
        raise click.ClickException(_format_http_error(exc))

    success(f"team '{created.name}' registered successfully (id: {created.id})")
