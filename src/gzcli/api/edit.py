from gzcli.api._http import APIProfile, make_get, make_post, make_put
from gzcli.api.models.edit import (
    ChallengeInfoModel,
    AttachmentCreateModel,
    ChallengeUpdateModel,
    ChallengeEditDetailModel,
    FlagCreateModel,
)


def add_challenge(
    profile: APIProfile, game_id: int, body: ChallengeInfoModel
) -> ChallengeEditDetailModel:
    """
    API wrapper for `/api/edit/games/{id}/challenges/`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/POST/api/edit/games/{id}/challenges
    """
    resp = make_post(
        profile,
        f"/api/edit/games/{game_id}/challenges/",
        json=body.model_dump(exclude_none=True),
    )
    return ChallengeEditDetailModel.model_validate(resp.json())


def get_challenges(profile: APIProfile, game_id: int) -> list[ChallengeInfoModel]:
    """
    API wrapper for `/api/edit/games/{id}/challenges`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/GET/api/edit/games/{id}/challenges
    """
    resp = make_get(profile, f"/api/edit/games/{game_id}/challenges")
    return [ChallengeInfoModel.model_validate(item) for item in resp.json()]


def get_challenge(
    profile: APIProfile, game_id: int, challenge_id: int
) -> ChallengeEditDetailModel:
    """
    API wrapper for `/api/edit/games/{id}/challenges/{cId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/GET/api/edit/games/{id}/challenges/{cId}
    """
    resp = make_get(profile, f"/api/edit/games/{game_id}/challenges/{challenge_id}")
    return ChallengeEditDetailModel.model_validate(resp.json())


def update_challenge_info(
    profile: APIProfile, game_id: int, challenge_id: int, body: ChallengeUpdateModel
) -> ChallengeEditDetailModel:
    """
    API wrapper for `/api/edit/games/{id}/challenges/{cId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/PUT/api/edit/games/{id}/challenges/{cId}
    """

    resp = make_put(
        profile,
        f"/api/edit/games/{game_id}/challenges/{challenge_id}",
        json=body.model_dump(exclude_none=True),
    )
    return ChallengeEditDetailModel.model_validate(resp.json())


def update_challenge_attachments(
    profile: APIProfile, game_id: int, challenge_id: int, body: AttachmentCreateModel
):
    """
    API wrapper for `/api/edit/games/{id}/challenges/{cId}/attachment`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/POST/api/edit/games/{id}/challenges/{cId}/attachment
    """
    return make_post(
        profile,
        f"/api/edit/games/{game_id}/challenges/{challenge_id}/attachment",
        json=body.model_dump(exclude_none=True),
    )


def add_challenge_flags(
    profile: APIProfile, game_id: int, challenge_id: int, body: list[FlagCreateModel]
):
    """
    API wrapper for `/api/edit/games/{id}/challenges/{cId}/flags`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/POST/api/edit/games/{id}/challenges/{cId}/flags
    """
    return make_post(
        profile,
        f"/api/edit/games/{game_id}/challenges/{challenge_id}/flags",
        json=[flag.model_dump(exclude_none=True) for flag in body],
    )
