from gzcli.api._http import APIProfile, make_get
from gzcli.api.models.account import HashPowChallenge
from gzcli.api.models.info import (
    ClientCaptchaInfoModel,
    ClientConfig,
    PostDetailModel,
    PostInfoModel,
)


def get_latest_posts(profile: APIProfile) -> list[PostInfoModel]:
    """
    API wrapper for `/api/posts/latest`
    docs: https://gzctf.gzti.me/scalar.html#tag/info/GET/api/posts/latest
    """
    resp = make_get(profile, "/api/posts/latest")
    return [PostInfoModel.model_validate(item) for item in resp.json()]


def get_posts(profile: APIProfile) -> list[PostInfoModel]:
    """
    API wrapper for `/api/posts`
    docs: https://gzctf.gzti.me/scalar.html#tag/info/GET/api/posts
    """
    resp = make_get(profile, "/api/posts")
    return [PostInfoModel.model_validate(item) for item in resp.json()]


def get_post(profile: APIProfile, id: str) -> PostDetailModel:
    """
    API wrapper for `/api/posts/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/info/GET/api/posts/{id}
    """
    resp = make_get(profile, f"/api/posts/{id}")
    return PostDetailModel.model_validate(resp.json())


def get_client_config(profile: APIProfile) -> ClientConfig:
    """
    API wrapper for `/api/config`
    docs: https://gzctf.gzti.me/scalar.html#tag/info/GET/api/config
    """
    resp = make_get(profile, "/api/config")
    return ClientConfig.model_validate(resp.json())


def get_client_captcha_info(profile: APIProfile) -> ClientCaptchaInfoModel:
    """
    API wrapper for `/api/captcha`
    docs: https://gzctf.gzti.me/scalar.html#tag/info/GET/api/captcha
    """
    resp = make_get(profile, "/api/captcha")
    return ClientCaptchaInfoModel.model_validate(resp.json())


def get_pow_challenge(profile: APIProfile) -> HashPowChallenge:
    """
    API wrapper for `/api/captcha/powchallenge`
    docs: https://gzctf.gzti.me/scalar.html#tag/info/GET/api/captcha/powchallenge
    """
    resp = make_get(profile, "/api/captcha/powchallenge")
    return HashPowChallenge.model_validate(resp.json())
