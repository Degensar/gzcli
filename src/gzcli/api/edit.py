from pathlib import Path

from gzcli.api._http import (
    APIProfile,
    make_get,
    make_post,
    make_put,
    make_delete,
)
from gzcli.api.models.data import ArrayResponse
from gzcli.api.models.edit import (
    ChallengeInfoModel,
    AttachmentCreateModel,
    ChallengeUpdateModel,
    ChallengeEditDetailModel,
    Division,
    DivisionCreateModel,
    DivisionEditModel,
    FlagCreateModel,
    GameInfoModel,
    GameNoticeModel,
    PostEditModel,
)
from gzcli.api.models.game import ContainerInfoModel, GameNotice
from gzcli.api.models.info import PostDetailModel


def add_challenge(
    profile: APIProfile, game_id: int, body: ChallengeInfoModel
) -> ChallengeEditDetailModel:
    """
    API wrapper for `/api/edit/games/{id}/challenges/`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/POST/api/edit/games/{id}/challenges
    """
    resp = make_post(
        profile,
        f"/api/edit/games/{game_id}/challenges",
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


def add_post(profile: APIProfile, body: PostEditModel) -> str:
    """
    API wrapper for `/api/edit/posts`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/POST/api/edit/posts
    """
    resp = make_post(
        profile,
        "/api/edit/posts",
        json=body.model_dump(exclude_none=True),
    )
    return resp.json()


def update_post(
    profile: APIProfile, post_id: str, body: PostEditModel
) -> PostDetailModel:
    """
    API wrapper for `/api/edit/posts/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/PUT/api/edit/posts/{id}
    """
    resp = make_put(
        profile,
        f"/api/edit/posts/{post_id}",
        json=body.model_dump(exclude_none=True),
    )
    return PostDetailModel.model_validate(resp.json())


def delete_post(profile: APIProfile, post_id: str):
    """
    API wrapper for `/api/edit/posts/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/DELETE/api/edit/posts/{id}
    """
    return make_delete(profile, f"/api/edit/posts/{post_id}")


def add_game(profile: APIProfile, body: GameInfoModel) -> GameInfoModel:
    """
    API wrapper for `/api/edit/games`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/POST/api/edit/games
    """
    resp = make_post(
        profile,
        "/api/edit/games",
        json=body.model_dump(exclude_none=True),
    )
    return GameInfoModel.model_validate(resp.json())


def get_games(
    profile: APIProfile, count: int = 50, skip: int = 0
) -> ArrayResponse[GameInfoModel]:
    """
    API wrapper for `/api/edit/games`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/GET/api/edit/games
    """
    resp = make_get(
        profile,
        "/api/edit/games",
        params={"count": count, "skip": skip},
    )
    return ArrayResponse[GameInfoModel].model_validate(resp.json())


def get_game(profile: APIProfile, game_id: int) -> GameInfoModel:
    """
    API wrapper for `/api/edit/games/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/GET/api/edit/games/{id}
    """
    resp = make_get(profile, f"/api/edit/games/{game_id}")
    return GameInfoModel.model_validate(resp.json())


def update_game(
    profile: APIProfile, game_id: int, body: GameInfoModel
) -> GameInfoModel:
    """
    API wrapper for `/api/edit/games/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/PUT/api/edit/games/{id}
    """
    resp = make_put(
        profile,
        f"/api/edit/games/{game_id}",
        json=body.model_dump(exclude_none=True),
    )
    return GameInfoModel.model_validate(resp.json())


def delete_game(profile: APIProfile, game_id: int):
    """
    API wrapper for `/api/edit/games/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/DELETE/api/edit/games/{id}

    The server returns an empty 200 body on success, so the raw response is returned.
    """
    return make_delete(profile, f"/api/edit/games/{game_id}")


def update_game_poster(profile: APIProfile, game_id: int, file: Path) -> str:
    """
    API wrapper for `/api/edit/games/{id}/poster`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/PUT/api/edit/games/{id}/poster
    """
    resp = make_put(
        profile,
        f"/api/edit/games/{game_id}/poster",
        files=[("file", file.open("rb"))],
    )
    return resp.json()


def add_notice(
    profile: APIProfile, game_id: int, body: GameNoticeModel
) -> GameNotice:
    """
    API wrapper for `/api/edit/games/{id}/notices`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/POST/api/edit/games/{id}/notices
    """
    resp = make_post(
        profile,
        f"/api/edit/games/{game_id}/notices",
        json=body.model_dump(exclude_none=True),
    )
    return GameNotice.model_validate(resp.json())


def get_notices(profile: APIProfile, game_id: int) -> list[GameNotice]:
    """
    API wrapper for `/api/edit/games/{id}/notices`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/GET/api/edit/games/{id}/notices
    """
    resp = make_get(profile, f"/api/edit/games/{game_id}/notices")
    return [GameNotice.model_validate(item) for item in resp.json()]


def update_notice(
    profile: APIProfile, game_id: int, notice_id: int, body: GameNoticeModel
) -> GameNotice:
    """
    API wrapper for `/api/edit/games/{id}/notices/{noticeId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/PUT/api/edit/games/{id}/notices/{noticeId}
    """
    resp = make_put(
        profile,
        f"/api/edit/games/{game_id}/notices/{notice_id}",
        json=body.model_dump(exclude_none=True),
    )
    return GameNotice.model_validate(resp.json())


def delete_notice(profile: APIProfile, game_id: int, notice_id: int):
    """
    API wrapper for `/api/edit/games/{id}/notices/{noticeId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/DELETE/api/edit/games/{id}/notices/{noticeId}
    """
    return make_delete(profile, f"/api/edit/games/{game_id}/notices/{notice_id}")


def add_division(
    profile: APIProfile, game_id: int, body: DivisionCreateModel
) -> Division:
    """
    API wrapper for `/api/edit/games/{id}/divisions`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/POST/api/edit/games/{id}/divisions
    """
    resp = make_post(
        profile,
        f"/api/edit/games/{game_id}/divisions",
        json=body.model_dump(exclude_none=True),
    )
    return Division.model_validate(resp.json())


def get_divisions(profile: APIProfile, game_id: int) -> list[Division]:
    """
    API wrapper for `/api/edit/games/{id}/divisions`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/GET/api/edit/games/{id}/divisions
    """
    resp = make_get(profile, f"/api/edit/games/{game_id}/divisions")
    return [Division.model_validate(item) for item in resp.json()]


def update_division(
    profile: APIProfile, game_id: int, division_id: int, body: DivisionEditModel
) -> Division:
    """
    API wrapper for `/api/edit/games/{id}/divisions/{divisionId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/PUT/api/edit/games/{id}/divisions/{divisionId}
    """
    resp = make_put(
        profile,
        f"/api/edit/games/{game_id}/divisions/{division_id}",
        json=body.model_dump(exclude_none=True),
    )
    return Division.model_validate(resp.json())


def delete_division(profile: APIProfile, game_id: int, division_id: int):
    """
    API wrapper for `/api/edit/games/{id}/divisions/{divisionId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/DELETE/api/edit/games/{id}/divisions/{divisionId}
    """
    return make_delete(
        profile, f"/api/edit/games/{game_id}/divisions/{division_id}"
    )


def flush_scoreboard(profile: APIProfile, game_id: int):
    """
    API wrapper for `/api/edit/games/{id}/scoreboard/flush`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/POST/api/edit/games/{id}/scoreboard/flush
    """
    return make_post(profile, f"/api/edit/games/{game_id}/scoreboard/flush")


def create_test_container(
    profile: APIProfile, game_id: int, challenge_id: int
) -> ContainerInfoModel:
    """
    API wrapper for `/api/edit/games/{id}/challenges/{cId}/container`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/POST/api/edit/games/{id}/challenges/{cId}/container
    """
    resp = make_post(
        profile,
        f"/api/edit/games/{game_id}/challenges/{challenge_id}/container",
    )
    return ContainerInfoModel.model_validate(resp.json())


def delete_test_container(profile: APIProfile, game_id: int, challenge_id: int):
    """
    API wrapper for `/api/edit/games/{id}/challenges/{cId}/container`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/DELETE/api/edit/games/{id}/challenges/{cId}/container
    """
    return make_delete(
        profile,
        f"/api/edit/games/{game_id}/challenges/{challenge_id}/container",
    )


def delete_challenge(profile: APIProfile, game_id: int, challenge_id: int):
    """
    API wrapper for `/api/edit/games/{id}/challenges/{cId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/DELETE/api/edit/games/{id}/challenges/{cId}
    """
    return make_delete(
        profile, f"/api/edit/games/{game_id}/challenges/{challenge_id}"
    )


def delete_flag(
    profile: APIProfile, game_id: int, challenge_id: int, flag_id: int
):
    """
    API wrapper for `/api/edit/games/{id}/challenges/{cId}/flags/{fId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/edit/DELETE/api/edit/games/{id}/challenges/{cId}/flags/{fId}
    """
    return make_delete(
        profile,
        f"/api/edit/games/{game_id}/challenges/{challenge_id}/flags/{flag_id}",
    )
