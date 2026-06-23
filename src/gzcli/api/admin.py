from pathlib import Path
from gzcli.api._http import APIProfile, make_get, make_post, make_put, make_delete
from gzcli.api.models.account import ProfileUserInfoModel
from gzcli.api.models.admin import (
    AdminTeamModel,
    AdminUserInfoModel,
    ConfigEditModel,
    ContainerInstanceModel,
    LogMessageModel,
    ParticipationEditModel,
    UserCreateModel,
    UserInfoModel,
    WriteupInfoModel,
)
from gzcli.api.models.data import ArrayResponse, LocalFile
from gzcli.api.models.info import TeamInfoModel


def get_config(profile: APIProfile) -> ConfigEditModel:
    """
    API wrapper for `/api/admin/config`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/GET/api/admin/config
    """
    resp = make_get(profile, "/api/admin/config")
    return ConfigEditModel.model_validate(resp.json())


def update_config(profile: APIProfile, body: ConfigEditModel):
    """
    API wrapper for `/api/admin/config`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/PUT/api/admin/config
    """
    return make_put(
        profile,
        "/api/admin/config",
        json=body.model_dump(exclude_none=True),
    )


def add_users(profile: APIProfile, body: list[UserCreateModel]):
    """
    API wrapper for `/api/admin/users`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/POST/api/admin/users
    """
    return make_post(
        profile,
        "/api/admin/users",
        json=[user.model_dump(exclude_none=True) for user in body],
    )


def get_users(
    profile: APIProfile, count: int = 100, skip: int = 0
) -> ArrayResponse[UserInfoModel]:
    """
    API wrapper for `/api/admin/users`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/GET/api/admin/users
    """
    resp = make_get(
        profile,
        "/api/admin/users",
        params={"count": count, "skip": skip},
    )
    return ArrayResponse[UserInfoModel].model_validate(resp.json())


def search_users(profile: APIProfile, hint: str) -> ArrayResponse[UserInfoModel]:
    """
    API wrapper for `/api/admin/users/search`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/POST/api/admin/users/search
    """
    resp = make_post(
        profile,
        "/api/admin/users/search",
        params={"hint": hint},
    )
    return ArrayResponse[UserInfoModel].model_validate(resp.json())


def get_teams(
    profile: APIProfile, count: int = 100, skip: int = 0
) -> ArrayResponse[TeamInfoModel]:
    """
    API wrapper for `/api/admin/teams`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/GET/api/admin/teams
    """
    resp = make_get(
        profile,
        "/api/admin/teams",
        params={"count": count, "skip": skip},
    )
    return ArrayResponse[TeamInfoModel].model_validate(resp.json())


def search_teams(profile: APIProfile, hint: str) -> ArrayResponse[TeamInfoModel]:
    """
    API wrapper for `/api/admin/teams/search`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/POST/api/admin/teams/search
    """
    resp = make_post(
        profile,
        "/api/admin/teams/search",
        params={"hint": hint},
    )
    return ArrayResponse[TeamInfoModel].model_validate(resp.json())


def update_team(profile: APIProfile, id: int, body: AdminTeamModel):
    """
    API wrapper for `/api/admin/teams/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/PUT/api/admin/teams/{id}
    """
    return make_put(
        profile,
        f"/api/admin/teams/{id}",
        json=body.model_dump(exclude_none=True),
    )


def update_user(profile: APIProfile, user_id: str, body: AdminUserInfoModel):
    """
    API wrapper for `/api/admin/users/{userid}`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/PUT/api/admin/users/{userid}
    """
    return make_put(
        profile,
        f"/api/admin/users/{user_id}",
        json=body.model_dump(exclude_none=True),
    )


def get_user(profile: APIProfile, user_id: str) -> ProfileUserInfoModel:
    """
    API wrapper for `/api/admin/users/{userid}`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/GET/api/admin/users/{userid}
    """
    resp = make_get(profile, f"/api/admin/users/{user_id}")
    return ProfileUserInfoModel.model_validate(resp.json())


def delete_user(profile: APIProfile, user_id: str):
    """
    API wrapper for `/api/admin/users/{userid}`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/DELETE/api/admin/users/{userid}

    The server returns an empty 200 body, so the raw response is returned.
    """
    return make_delete(profile, f"/api/admin/users/{user_id}")


def reset_user_password(profile: APIProfile, user_id: str) -> str:
    """
    API wrapper for `/api/admin/users/{userid}/password`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/DELETE/api/admin/users/{userid}/password
    """
    resp = make_delete(profile, f"/api/admin/users/{user_id}/password")
    return resp.json()


def delete_team(profile: APIProfile, id: int):
    """
    API wrapper for `/api/admin/teams/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/DELETE/api/admin/teams/{id}

    The server returns an empty 200 body, so the raw response is returned.
    """
    return make_delete(profile, f"/api/admin/teams/{id}")


def get_logs(
    profile: APIProfile, level: str = "All", count: int = 50, skip: int = 0
) -> list[LogMessageModel]:
    """
    API wrapper for `/api/admin/logs`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/GET/api/admin/logs
    """
    resp = make_get(
        profile,
        "/api/admin/logs",
        params={"level": level, "count": count, "skip": skip},
    )
    return [LogMessageModel.model_validate(item) for item in resp.json()]


def update_participation(profile: APIProfile, id: int, body: ParticipationEditModel):
    """
    API wrapper for `/api/admin/participation/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/PUT/api/admin/participation/{id}
    """
    return make_put(
        profile,
        f"/api/admin/participation/{id}",
        json=body.model_dump(exclude_none=True),
    )


def get_writeups(profile: APIProfile, id: int) -> WriteupInfoModel:
    """
    API wrapper for `/api/admin/writeups/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/GET/api/admin/writeups/{id}
    """
    resp = make_get(profile, f"/api/admin/writeups/{id}")
    return WriteupInfoModel.model_validate(resp.json())


def get_instances(profile: APIProfile) -> ArrayResponse[ContainerInstanceModel]:
    """
    API wrapper for `/api/admin/instances`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/GET/api/admin/instances
    """
    resp = make_get(profile, "/api/admin/instances")
    return ArrayResponse[ContainerInstanceModel].model_validate(resp.json())


def delete_instance(profile: APIProfile, id: str):
    """
    API wrapper for `/api/admin/instances/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/DELETE/api/admin/instances/{id}
    """
    return make_delete(profile, f"/api/admin/instances/{id}")


def get_files(
    profile: APIProfile, count: int = 50, skip: int = 0
) -> ArrayResponse[LocalFile]:
    """
    API wrapper for `/api/admin/files`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/GET/api/admin/files
    """
    resp = make_get(
        profile,
        "/api/admin/files",
        params={"count": count, "skip": skip},
    )
    return ArrayResponse[LocalFile].model_validate(resp.json())


def update_logo(profile: APIProfile, file: Path):
    """
    API wrapper for `/api/admin/config/logo`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/POST/api/admin/config/logo

    The server returns an empty 200 body, so the raw response is returned.
    """
    with file.open("rb") as fh:
        return make_post(
            profile,
            "/api/admin/config/logo",
            files=[("file", fh)],
        )


def reset_logo(profile: APIProfile):
    """
    API wrapper for `/api/admin/config/logo`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/DELETE/api/admin/config/logo

    The server returns an empty 200 body, so the raw response is returned.
    """
    return make_delete(profile, "/api/admin/config/logo")


def download_all_writeups(profile: APIProfile, id: int):
    """
    API wrapper for `/api/admin/writeups/{id}/all`
    docs: https://gzctf.gzti.me/scalar.html#tag/admin/GET/api/admin/writeups/{id}/all

    Returns a tar download, so the raw response is returned.
    """
    return make_get(profile, f"/api/admin/writeups/{id}/all")
