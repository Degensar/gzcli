from pathlib import Path

from gzcli.api._http import (
    APIProfile,
    make_get,
    make_post,
    make_put,
    make_delete,
)
from gzcli.api.models.info import (
    TeamUpdateModel,
    TeamInfoModel,
    TeamTransferModel,
    SignatureVerifyModel,
)


def create_team(profile: APIProfile, body: TeamUpdateModel) -> TeamInfoModel:
    """
    API wrapper for `/api/team`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/POST/api/team
    """
    resp = make_post(
        profile,
        "/api/team",
        json=body.model_dump(exclude_none=True),
    )
    return TeamInfoModel.model_validate(resp.json())


def get_team(profile: APIProfile, id: int) -> TeamInfoModel:
    """
    API wrapper for `/api/team/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/GET/api/team/{id}
    """
    resp = make_get(profile, f"/api/team/{id}")
    return TeamInfoModel.model_validate(resp.json())


def get_teams(profile: APIProfile) -> list[TeamInfoModel]:
    """
    API wrapper for `/api/team`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/GET/api/team
    """
    resp = make_get(profile, "/api/team")
    return [TeamInfoModel.model_validate(item) for item in resp.json()]


def update_team(
    profile: APIProfile, id: int, body: TeamUpdateModel
) -> TeamInfoModel:
    """
    API wrapper for `/api/team/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/PUT/api/team/{id}
    """
    resp = make_put(
        profile,
        f"/api/team/{id}",
        json=body.model_dump(exclude_none=True),
    )
    return TeamInfoModel.model_validate(resp.json())


def transfer_team(
    profile: APIProfile, id: int, body: TeamTransferModel
) -> TeamInfoModel:
    """
    API wrapper for `/api/team/{id}/transfer`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/PUT/api/team/{id}/transfer
    """
    resp = make_put(
        profile,
        f"/api/team/{id}/transfer",
        json=body.model_dump(exclude_none=True),
    )
    return TeamInfoModel.model_validate(resp.json())


def get_invite_code(profile: APIProfile, id: int) -> str:
    """
    API wrapper for `/api/team/{id}/invite`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/GET/api/team/{id}/invite
    """
    resp = make_get(profile, f"/api/team/{id}/invite")
    return resp.json()


def update_invite_code(profile: APIProfile, id: int) -> str:
    """
    API wrapper for `/api/team/{id}/invite`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/PUT/api/team/{id}/invite
    """
    resp = make_put(profile, f"/api/team/{id}/invite")
    return resp.json()


def kick_user(profile: APIProfile, id: int, user_id: str) -> TeamInfoModel:
    """
    API wrapper for `/api/team/{id}/kick/{userId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/POST/api/team/{id}/kick/{userId}
    """
    resp = make_post(profile, f"/api/team/{id}/kick/{user_id}")
    return TeamInfoModel.model_validate(resp.json())


def accept_invite(profile: APIProfile, code: str):
    """
    API wrapper for `/api/team/accept`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/POST/api/team/accept
    """
    return make_post(profile, "/api/team/accept", json=code)


def leave_team(profile: APIProfile, id: int):
    """
    API wrapper for `/api/team/{id}/leave`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/POST/api/team/{id}/leave
    """
    return make_post(profile, f"/api/team/{id}/leave")


def update_avatar(profile: APIProfile, id: int, file: Path) -> str:
    """
    API wrapper for `/api/team/{id}/avatar`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/PUT/api/team/{id}/avatar
    """
    with file.open("rb") as fh:
        resp = make_put(
            profile,
            f"/api/team/{id}/avatar",
            files=[("file", fh)],
        )
    return resp.json()


def delete_team(profile: APIProfile, id: int):
    """
    API wrapper for `/api/team/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/DELETE/api/team/{id}

    The server returns an empty 200 body, so the raw response is returned.
    """
    return make_delete(profile, f"/api/team/{id}")


def verify_signature(profile: APIProfile, body: SignatureVerifyModel):
    """
    API wrapper for `/api/team/verify`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/POST/api/team/verify
    """
    return make_post(
        profile,
        "/api/team/verify",
        json=body.model_dump(exclude_none=True),
    )
