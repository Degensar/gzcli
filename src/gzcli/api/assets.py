import contextlib
from pathlib import Path
from typing import Iterable, Optional
from gzcli.api._http import APIProfile, make_get, make_post, make_delete
from gzcli.api.models.data import LocalFile


def upload_files(
    profile: APIProfile,
    file_paths: Iterable[Path],
    filename: Optional[str] = None,
) -> list[LocalFile]:
    """
    API wrapper for `/api/assets`
    docs: https://gzctf.gzti.me/scalar.html#tag/assets/POST/api/assets
    """
    with contextlib.ExitStack() as stack:
        resp = make_post(
            profile,
            "/api/assets",
            params={"filename": filename} if filename else None,
            files=[
                ("files", stack.enter_context(f.open(mode="rb"))) for f in file_paths
            ],
        )
    return [LocalFile.model_validate(item) for item in resp.json()]


def get_file(profile: APIProfile, hash: str, filename: str):
    """
    API wrapper for `/assets/{hash}/{filename}`
    docs: https://gzctf.gzti.me/scalar.html#tag/assets/GET/assets/{hash}/{filename}
    """
    return make_get(profile, f"/assets/{hash}/{filename}")


def delete_file(profile: APIProfile, hash: str):
    """
    API wrapper for `/api/assets/{hash}`
    docs: https://gzctf.gzti.me/scalar.html#tag/assets/DELETE/api/assets/{hash}
    """
    return make_delete(profile, f"/api/assets/{hash}")
