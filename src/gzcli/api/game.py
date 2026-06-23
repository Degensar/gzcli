from pathlib import Path
from typing import Optional

from gzcli.api._http import APIProfile, make_get, make_post, make_delete
from gzcli.api.models.data import ArrayResponse
from gzcli.api.models.enum import AnswerResult
from gzcli.api.models.game import (
    BasicGameInfoModel,
    BasicWriteupInfoModel,
    ChallengeDetailModel,
    CheatInfoModel,
    ContainerInfoModel,
    DetailedGameInfoModel,
    GameEvent,
    GameJoinCheckInfoModel,
    GameJoinModel,
    GameNotice,
    GameDetailModel,
    FlagSubmitModel,
    ScoreboardModel,
    Submission,
)
from gzcli.api.models.admin import ParticipationInfoModel


def get_recent_games(profile: APIProfile, limit: int = 0) -> list[BasicGameInfoModel]:
    """
    API wrapper for `/api/game/recent`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/recent
    """
    resp = make_get(profile, "/api/game/recent", params={"limit": limit})
    return [BasicGameInfoModel.model_validate(item) for item in resp.json()]


def get_games(
    profile: APIProfile, count: int = 10, skip: int = 0
) -> ArrayResponse[BasicGameInfoModel]:
    """
    API wrapper for `/api/game`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game
    """
    resp = make_get(profile, "/api/game", params={"count": count, "skip": skip})
    return ArrayResponse[BasicGameInfoModel].model_validate(resp.json())


def get_game(profile: APIProfile, game_id: int) -> DetailedGameInfoModel:
    """
    API wrapper for `/api/game/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}
    """
    resp = make_get(profile, f"/api/game/{game_id}")
    return DetailedGameInfoModel.model_validate(resp.json())


def check_game(profile: APIProfile, game_id: int) -> GameJoinCheckInfoModel:
    """
    API wrapper for `/api/game/{id}/check`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/check
    """
    resp = make_get(profile, f"/api/game/{game_id}/check")
    return GameJoinCheckInfoModel.model_validate(resp.json())


def join_game(profile: APIProfile, game_id: int, body: GameJoinModel):
    """
    API wrapper for `/api/game/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/POST/api/game/{id}
    """
    return make_post(
        profile,
        f"/api/game/{game_id}",
        json=body.model_dump(exclude_none=True),
    )


def leave_game(profile: APIProfile, game_id: int):
    """
    API wrapper for `/api/game/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/DELETE/api/game/{id}
    """
    return make_delete(profile, f"/api/game/{game_id}")


def get_scoreboard(profile: APIProfile, game_id: int) -> ScoreboardModel:
    """
    API wrapper for `/api/game/{id}/scoreboard`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/scoreboard
    """
    resp = make_get(profile, f"/api/game/{game_id}/scoreboard")
    return ScoreboardModel.model_validate(resp.json())


def get_notices(
    profile: APIProfile, game_id: int, count: int = 100, skip: int = 0
) -> list[GameNotice]:
    """
    API wrapper for `/api/game/{id}/notices`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/notices
    """
    resp = make_get(
        profile,
        f"/api/game/{game_id}/notices",
        params={"count": count, "skip": skip},
    )
    return [GameNotice.model_validate(item) for item in resp.json()]


def get_events(
    profile: APIProfile,
    game_id: int,
    hide_container: bool = False,
    count: int = 100,
    skip: int = 0,
) -> list[GameEvent]:
    """
    API wrapper for `/api/game/{id}/events`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/events
    """
    resp = make_get(
        profile,
        f"/api/game/{game_id}/events",
        params={"hideContainer": hide_container, "count": count, "skip": skip},
    )
    return [GameEvent.model_validate(item) for item in resp.json()]


def get_submissions(
    profile: APIProfile,
    game_id: int,
    type: Optional[AnswerResult] = None,
    count: int = 100,
    skip: int = 0,
) -> list[Submission]:
    """
    API wrapper for `/api/game/{id}/submissions`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/submissions
    """
    params: dict = {"count": count, "skip": skip}
    if type is not None:
        params["type"] = type
    resp = make_get(profile, f"/api/game/{game_id}/submissions", params=params)
    return [Submission.model_validate(item) for item in resp.json()]


def get_cheat_info(profile: APIProfile, game_id: int) -> list[CheatInfoModel]:
    """
    API wrapper for `/api/game/{id}/cheatinfo`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/cheatinfo
    """
    resp = make_get(profile, f"/api/game/{game_id}/cheatinfo")
    return [CheatInfoModel.model_validate(item) for item in resp.json()]


def get_game_details(profile: APIProfile, game_id: int) -> GameDetailModel:
    """
    API wrapper for `/api/game/{id}/details`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/details
    """
    resp = make_get(profile, f"/api/game/{game_id}/details")
    return GameDetailModel.model_validate(resp.json())


def get_participations(
    profile: APIProfile, game_id: int
) -> list[ParticipationInfoModel]:
    """
    API wrapper for `/api/game/{id}/participations`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/participations
    """
    resp = make_get(profile, f"/api/game/{game_id}/participations")
    return [ParticipationInfoModel.model_validate(item) for item in resp.json()]


def get_challenge(
    profile: APIProfile, game_id: int, challenge_id: int
) -> ChallengeDetailModel:
    """
    API wrapper for `/api/game/{id}/challenges/{challengeId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/challenges/{challengeId}
    """
    resp = make_get(profile, f"/api/game/{game_id}/challenges/{challenge_id}")
    return ChallengeDetailModel.model_validate(resp.json())


def submit_flag(
    profile: APIProfile, game_id: int, challenge_id: int, body: FlagSubmitModel
) -> int:
    """
    API wrapper for `/api/game/{id}/challenges/{challengeId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/POST/api/game/{id}/challenges/{challengeId}
    """
    resp = make_post(
        profile,
        f"/api/game/{game_id}/challenges/{challenge_id}",
        json=body.model_dump(exclude_none=True),
    )
    return resp.json()


def get_submission_status(
    profile: APIProfile, game_id: int, challenge_id: int, submit_id: int
) -> AnswerResult:
    """
    API wrapper for `/api/game/{id}/challenges/{challengeId}/status/{submitId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/challenges/{challengeId}/status/{submitId}
    """
    resp = make_get(
        profile,
        f"/api/game/{game_id}/challenges/{challenge_id}/status/{submit_id}",
    )
    return resp.json()


def get_writeup(profile: APIProfile, game_id: int) -> BasicWriteupInfoModel:
    """
    API wrapper for `/api/game/{id}/writeup`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/writeup
    """
    resp = make_get(profile, f"/api/game/{game_id}/writeup")
    return BasicWriteupInfoModel.model_validate(resp.json())


def submit_writeup(profile: APIProfile, game_id: int, file: Path):
    """
    API wrapper for `/api/game/{id}/writeup`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/POST/api/game/{id}/writeup
    """
    return make_post(
        profile,
        f"/api/game/{game_id}/writeup",
        files=[("file", file.open("rb"))],
    )


def create_container(
    profile: APIProfile, game_id: int, challenge_id: int
) -> ContainerInfoModel:
    """
    API wrapper for `/api/game/{id}/container/{challengeId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/POST/api/game/{id}/container/{challengeId}
    """
    resp = make_post(profile, f"/api/game/{game_id}/container/{challenge_id}")
    return ContainerInfoModel.model_validate(resp.json())


def extend_container(
    profile: APIProfile, game_id: int, challenge_id: int
) -> ContainerInfoModel:
    """
    API wrapper for `/api/game/{id}/container/{challengeId}/extend`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/POST/api/game/{id}/container/{challengeId}/extend
    """
    resp = make_post(profile, f"/api/game/{game_id}/container/{challenge_id}/extend")
    return ContainerInfoModel.model_validate(resp.json())


def delete_container(profile: APIProfile, game_id: int, challenge_id: int):
    """
    API wrapper for `/api/game/{id}/container/{challengeId}`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/DELETE/api/game/{id}/container/{challengeId}
    """
    return make_delete(profile, f"/api/game/{game_id}/container/{challenge_id}")


def get_scoreboard_sheet(profile: APIProfile, game_id: int):
    """
    API wrapper for `/api/game/{id}/scoreboardsheet`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/scoreboardsheet
    """
    return make_get(profile, f"/api/game/{game_id}/scoreboardsheet")


def get_submission_sheet(profile: APIProfile, game_id: int):
    """
    API wrapper for `/api/game/{id}/submissionsheet`
    docs: https://gzctf.gzti.me/scalar.html#tag/game/GET/api/game/{id}/submissionsheet
    """
    return make_get(profile, f"/api/game/{game_id}/submissionsheet")
