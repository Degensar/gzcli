from pathlib import Path

from gzcli.api._http import APIProfile, make_get, make_post, make_put
from gzcli.api.models.account import (
    AccountVerifyModel,
    LoginModel,
    MailChangeModel,
    PasswordChangeModel,
    PasswordResetModel,
    ProfileUpdateModel,
    ProfileUserInfoModel,
    RecoveryModel,
    RegisterModel,
)


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


def recover(profile: APIProfile, body: RecoveryModel):
    """
    API wrapper for `/api/account/recovery`
    docs: https://gzctf.gzti.me/scalar.html#tag/account/POST/api/account/recovery
    """
    return make_post(
        profile,
        "/api/account/recovery",
        json=body.model_dump(exclude_none=True),
    )


def reset_password(profile: APIProfile, body: PasswordResetModel):
    """
    API wrapper for `/api/account/passwordreset`
    docs: https://gzctf.gzti.me/scalar.html#tag/account/POST/api/account/passwordreset
    """
    return make_post(
        profile,
        "/api/account/passwordreset",
        json=body.model_dump(exclude_none=True),
    )


def verify(profile: APIProfile, body: AccountVerifyModel):
    """
    API wrapper for `/api/account/verify`
    docs: https://gzctf.gzti.me/scalar.html#tag/account/POST/api/account/verify
    """
    return make_post(
        profile,
        "/api/account/verify",
        json=body.model_dump(exclude_none=True),
    )


def login(profile: APIProfile, body: LoginModel):
    """
    API wrapper for `/api/account/login`
    docs: https://gzctf.gzti.me/scalar.html#tag/account/POST/api/account/login
    """
    return make_post(
        profile,
        "/api/account/login",
        json=body.model_dump(exclude_none=True),
    )


def logout(profile: APIProfile):
    """
    API wrapper for `/api/account/logout`
    docs: https://gzctf.gzti.me/scalar.html#tag/account/POST/api/account/logout
    """
    return make_post(
        profile,
        "/api/account/logout",
    )


def update_profile(profile: APIProfile, body: ProfileUpdateModel):
    """
    API wrapper for `/api/account/update`
    docs: https://gzctf.gzti.me/scalar.html#tag/account/PUT/api/account/update
    """
    return make_put(
        profile,
        "/api/account/update",
        json=body.model_dump(exclude_none=True),
    )


def change_password(profile: APIProfile, body: PasswordChangeModel):
    """
    API wrapper for `/api/account/changepassword`
    docs: https://gzctf.gzti.me/scalar.html#tag/account/PUT/api/account/changepassword
    """
    return make_put(
        profile,
        "/api/account/changepassword",
        json=body.model_dump(exclude_none=True),
    )


def change_email(profile: APIProfile, body: MailChangeModel):
    """
    API wrapper for `/api/account/changeemail`
    docs: https://gzctf.gzti.me/scalar.html#tag/account/PUT/api/account/changeemail
    """
    return make_put(
        profile,
        "/api/account/changeemail",
        json=body.model_dump(exclude_none=True),
    )


def confirm_mail_change(profile: APIProfile, body: AccountVerifyModel):
    """
    API wrapper for `/api/account/mailchangeconfirm`
    docs: https://gzctf.gzti.me/scalar.html#tag/account/POST/api/account/mailchangeconfirm
    """
    return make_post(
        profile,
        "/api/account/mailchangeconfirm",
        json=body.model_dump(exclude_none=True),
    )


def get_profile(profile: APIProfile) -> ProfileUserInfoModel:
    """
    API wrapper for `/api/account/profile`
    docs: https://gzctf.gzti.me/scalar.html#tag/account/GET/api/account/profile
    """
    resp = make_get(profile, "/api/account/profile")
    return ProfileUserInfoModel.model_validate(resp.json())


def update_avatar(profile: APIProfile, file: Path) -> str:
    """
    API wrapper for `/api/account/avatar`
    docs: https://gzctf.gzti.me/scalar.html#tag/account/PUT/api/account/avatar
    """
    resp = make_put(
        profile,
        "/api/account/avatar",
        files=[("file", file.open("rb"))],
    )
    return resp.json()
