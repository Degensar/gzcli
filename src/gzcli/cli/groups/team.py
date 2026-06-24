"""Commands for managing teams on the remote ctf server"""

import click
from pydantic import ValidationError
from gzcli.cli.auth import require_existing_profile, APIProfile
from gzcli.cli.errors import error_wrap, format_validation_error
from gzcli.cli.output import success
from gzcli.api.team import create_team
from gzcli.api.models.info import TeamUpdateModel


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
        raise click.ClickException(
            f"invalid team information: {format_validation_error(exc)}"
        )

    created = create_team(profile, body)
    success(f"team '{created.name}' registered successfully (id: {created.id})")
