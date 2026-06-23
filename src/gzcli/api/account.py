from gzcli.api._http import APIProfile, make_post
from gzcli.api.models.account import RegisterModel


def register(profile: APIProfile, body: RegisterModel):
    """
    API wrapper for `/api/account/register`
    docs: https://gzctf.gzti.me/scalar.html#tag/account/POST/api/account/register
    """
    return make_post(
        profile,
        "/api/account/register",
        json=body.model_dump(exclude_none=True),
    )
