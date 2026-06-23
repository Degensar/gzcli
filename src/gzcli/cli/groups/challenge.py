"""Helper commands for building challenges locally"""

import click
from pathlib import Path
from gzcli.cli.config import CLI_PATH
from gzcli.cli.errors import error_wrap
from gzcli.cli.models import ChallengeSpec
from gzcli.cli.output import success


@click.group()
def challenge():
    pass


@challenge.command()
@click.option("-n", "--name", required=True)
@click.argument(
    "dest",
    type=click.Path(file_okay=False, writable=True, path_type=Path),
)
@click.option("-t", "--template", default="default")
@error_wrap
def init(name, dest: Path, template: str = "default"):
    dest.mkdir(parents=True, exist_ok=True)
    templates_dir = CLI_PATH / "templates"
    if not templates_dir.is_dir():
        raise click.ClickException(f"template directory {templates_dir} does not exist")

    available_templates = {fp.name: fp for fp in templates_dir.iterdir() if fp.is_dir()}
    if not available_templates:
        raise click.ClickException(f"no templates available in {templates_dir}")

    if template not in available_templates:
        raise click.ClickException(
            f"invalid template name, available template names are: \n{'\n'.join(available_templates)}"
        )
    available_templates[template].copy_into(dest)
    success(f"initialized challenge files for {name} at {dest}/")


@challenge.command()
@click.argument(
    "challenge_directory",
    type=click.Path(file_okay=False, writable=True, path_type=Path),
)
@error_wrap
def build(challenge_directory: Path):
    pass


@challenge.command()
@click.argument("spec", type=click.File())
@error_wrap
def validate(spec: ChallengeSpec):
    pass
