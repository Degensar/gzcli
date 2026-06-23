"""Commands for interacting the games (CTF contests) on the remote ctf server"""

import hashlib
import click
import yaml
from pathlib import Path
from gzcli.cli.auth import require_existing_profile, APIProfile
from gzcli.cli.models import ChallengeSpec
from gzcli.cli.output import success, info
from gzcli.api.assets import upload_files
from gzcli.api.edit import (
    add_challenge,
    update_challenge_info,
    update_challenge_attachments,
    add_challenge_flags,
)
from gzcli.api.models.edit import (
    ChallengeInfoModel,
    ChallengeUpdateModel,
    AttachmentCreateModel,
    FlagCreateModel,
)

require_game_id = click.option("-g", "--game-id", "game_id", type=int, required=True)


def _parse_challenge_spec(spec_fp: Path):
    spec_text = yaml.safe_load(spec_fp.read_text())
    return ChallengeSpec.model_validate(spec_text)


@click.group()
def game():
    pass


@game.command()
@click.option("--title", required=True)
@click.option("--start-time", type=click.DateTime(), required=True)
@click.option("--end-time", type=click.DateTime(), required=True)
@require_existing_profile
def create(title: str, start_time: int, end_time: int, profile: APIProfile):
    """creates a new game on the remote CTF server"""
    raise click.ClickException("this command is currently unavailable")


@game.command()
@require_game_id
@require_existing_profile
def get(game_id: int, profile: APIProfile):
    """\b
    retreives game info from the remote CTF server.
    """
    pass


@game.command("push-challenge")
@click.argument(
    "challenge_path", type=click.Path(exists=True, file_okay=False, path_type=Path)
)
@require_game_id
@require_existing_profile
def push_challenge(game_id: int, challenge_path: Path, profile: APIProfile):
    """\b
    push a challenge to the remote CTF server.
    use `gz list-challenge-categories` to see the full list of challenge categories.
    use `gz list-challenge-types` to see the full list of challenge types.
    """
    spec_path = challenge_path / "challenge.yml"
    if not spec_path.is_file():
        spec_path = spec_path.with_suffix(".yaml")
    if not spec_path.is_file():
        raise click.ClickException(f"could not find challenge.yaml at {challenge_path}")

    spec = _parse_challenge_spec(spec_path)

    # dynamic types not supported for now
    if "Dynamic" in spec.deployment.deploymentType:
        raise click.ClickException("dynamic challenge is not supported yet.")

    add_challenge_body = ChallengeInfoModel(
        title=spec.title, type=spec.deployment.deploymentType, category=spec.category
    )
    resp = add_challenge(profile, game_id, add_challenge_body)
    challenge_id = resp.id

    # do not set isEnabled to true in this step as there is no flag yet
    update_info_body = ChallengeUpdateModel(
        content=spec.description,
        hints=spec.hints,
        difficulty=spec.scoring.difficulty,
        originalScore=spec.scoring.base_points,
        minScoreRate=spec.scoring.min_score_ratio,
        disableBloodBonus=spec.scoring.bloodBonus,
        submissionLimit=spec.maxAttempts,
    )
    if "Container" in spec.deployment.deploymentType:
        update_info_body.model_copy(update=spec.deployment.containers.flat())

    resp = update_challenge_info(profile, game_id, challenge_id, update_info_body)

    upload_files(profile, (challenge_path / i.path for i in spec.deployment.attachment))

    if "Static" in spec.deployment.deploymentType:
        # if the challenge attachment is static, only one attachment and one flag is allowed
        challenge_attachment = spec.deployment.attachment[0]
        update_attachment_body = AttachmentCreateModel(
            attachmentType=challenge_attachment.type
        )
        if challenge_attachment.type == "Local":
            file_hash = hashlib.sha256(
                (challenge_path / challenge_attachment.path).read_bytes()
            ).hexdigest()
            update_attachment_body.fileHash = file_hash
        elif challenge_attachment.type == "Remote":
            update_attachment_body.remoteUrl = challenge_attachment.path
        update_challenge_attachments(
            profile, game_id, challenge_id, update_attachment_body
        )
        update_flag_body = [
            FlagCreateModel(flag=flag, **update_attachment_body.model_dump())
            for flag in spec.flag
        ]
        add_challenge_flags(profile, game_id, challenge_id, update_flag_body)
    else:
        pass

    if not spec.hidden:
        update_challenge_info(
            profile, game_id, challenge_id, ChallengeUpdateModel(isEnabled=True)
        )

    challenge_endpoint = profile.make_endpoint(
        f"/admin/games/{game_id}/challenges/{challenge_id}"
    )
    success("challenge pushed successfully")
    info(f"access the challenge at {challenge_endpoint}")


# @game.command("upload-assets")
# @require_existing_profile
# @click.argument("files", type=click.Path(exists=True, dir_okay=False, path_type=Path), nargs=-1)
# def upload_assets(files: tuple[Path], profile: APIProfile):
#     from gzcli.api.assets import upload_file
#     upload_file(profile, files)
