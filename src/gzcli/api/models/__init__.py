"""Pydantic data models for the GZ::CTF API, grouped by API category.

Submodules attempts to mirror the ``src/GZCTF/models`` directory of the GZ::CTF source,
with some exceptions, in particular, models are located according to the following rules:

1. Enum types (``Literal`` aliases) are centralized in the ``enum`` submodule.
2. Data models that does not serve directly as request/response body but only a field of such will
   be located in the ``data`` submodule.
3. For models that serves as request/response body, if the exact model appears in the GZ::CTF source,
   it is then located at the same category as the source.
4. If the model does not appear in the source, it is then located at the *first* API category it appears in.
...

Every public model is re-exported here so callers can use either form:

    from gzcli.api.models import LoginModel
    from gzcli.api.models.account import LoginModel

"""

from . import account, admin, data, edit, enum, game, info

# --- enum -------------------------------------------------------------------
from .enum import (
    AnswerResult,
    CaptchaProvider,
    ChallengeCategory,
    ChallengeNetworkMode,
    ChallengeType,
    CompressionFormat,
    ContainerPortMappingType,
    ContainerStatus,
    Difficulty,
    ErrorCodes,
    EventType,
    FileType,
    GamePermission,
    NoticeType,
    ParticipationStatus,
    RegisterStatus,
    Role,
    SubmissionType,
    TaskStatus,
    TimeStamp,
)

# --- account ----------------------------------------------------------------
from .account import (
    AccountVerifyModel,
    HashPowChallenge,
    LoginModel,
    MailChangeModel,
    ModelWithCaptcha,
    PasswordChangeModel,
    PasswordResetModel,
    ProfileUpdateModel,
    ProfileUserInfoModel,
    RecoveryModel,
    RegisterModel,
)

# --- admin ------------------------------------------------------------------
from .admin import (
    AccountPolicy,
    AdminTeamModel,
    AdminUserInfoModel,
    ApiTokenCreateModel,
    ApiTokenResponse,
    ChallengeModel,
    ConfigEditModel,
    ContainerInstanceModel,
    ContainerPolicy,
    GlobalConfig,
    LogMessageModel,
    ParticipationEditModel,
    ParticipationInfoModel,
    TeamWithDetailedUserInfo,
    UserCreateModel,
    UserInfoModel,
    WriteupInfo,
    WriteupInfoModel,
)

# --- data -------------------------------------------------------------------
from .data import (
    ApiToken,
    ArrayResponse,
    Attachment,
    Blood,
    BloodBonus,
    ChallengeItem,
    DivisionChallengeItem,
    DivisionInfo,
    DivisionItem,
    JoinedTeam,
    LocalFile,
    RequestResponse,
    ScoreboardItem,
    TimeLine,
    TimeLineItem,
    TopTimeLine,
)

# --- edit -------------------------------------------------------------------
from .edit import (
    AttachmentCreateModel,
    ChallengeEditDetailModel,
    ChallengeInfoModel,
    ChallengeUpdateModel,
    Division,
    DivisionChallengeConfigModel,
    DivisionCreateModel,
    DivisionEditModel,
    FlagCreateModel,
    FlagInfoModel,
    GameInfoModel,
    GameNoticeModel,
    PostEditModel,
)

# --- game -------------------------------------------------------------------
from .game import (
    BasicGameInfoModel,
    BasicWriteupInfoModel,
    ChallengeDetailModel,
    ChallengeInfo,
    ChallengeTrafficModel,
    CheatInfoModel,
    ClientFlagContext,
    ContainerInfoModel,
    DetailedGameInfoModel,
    FileRecord,
    FlagSubmitModel,
    GameDetailModel,
    GameEvent,
    GameJoinCheckInfoModel,
    GameJoinModel,
    GameNotice,
    ParticipationModel,
    ScoreboardModel,
    Submission,
    TeamModel,
    TeamTrafficModel,
)

# --- info -------------------------------------------------------------------
from .info import (
    ClientCaptchaInfoModel,
    ClientConfig,
    PostDetailModel,
    PostInfoModel,
    SignatureVerifyModel,
    TeamInfoModel,
    TeamTransferModel,
    TeamUpdateModel,
    TeamUserInfoModel,
)

__all__ = [
    # submodules
    "account",
    "admin",
    "data",
    "edit",
    "enum",
    "game",
    "info",
    # enum
    "AnswerResult",
    "CaptchaProvider",
    "ChallengeCategory",
    "ChallengeNetworkMode",
    "ChallengeType",
    "CompressionFormat",
    "ContainerPortMappingType",
    "ContainerStatus",
    "Difficulty",
    "ErrorCodes",
    "EventType",
    "FileType",
    "GamePermission",
    "NoticeType",
    "ParticipationStatus",
    "RegisterStatus",
    "Role",
    "SubmissionType",
    "TaskStatus",
    "TimeStamp",
    # account
    "AccountVerifyModel",
    "HashPowChallenge",
    "LoginModel",
    "MailChangeModel",
    "ModelWithCaptcha",
    "PasswordChangeModel",
    "PasswordResetModel",
    "ProfileUpdateModel",
    "ProfileUserInfoModel",
    "RecoveryModel",
    "RegisterModel",
    # admin
    "AccountPolicy",
    "AdminTeamModel",
    "AdminUserInfoModel",
    "ApiTokenCreateModel",
    "ApiTokenResponse",
    "ChallengeModel",
    "ConfigEditModel",
    "ContainerInstanceModel",
    "ContainerPolicy",
    "GlobalConfig",
    "LogMessageModel",
    "ParticipationEditModel",
    "ParticipationInfoModel",
    "TeamWithDetailedUserInfo",
    "UserCreateModel",
    "UserInfoModel",
    "WriteupInfo",
    "WriteupInfoModel",
    # data
    "ApiToken",
    "ArrayResponse",
    "Attachment",
    "Blood",
    "BloodBonus",
    "ChallengeItem",
    "DivisionChallengeItem",
    "DivisionInfo",
    "DivisionItem",
    "JoinedTeam",
    "LocalFile",
    "RequestResponse",
    "ScoreboardItem",
    "TimeLine",
    "TimeLineItem",
    "TopTimeLine",
    # edit
    "AttachmentCreateModel",
    "ChallengeEditDetailModel",
    "ChallengeInfoModel",
    "ChallengeUpdateModel",
    "Division",
    "DivisionChallengeConfigModel",
    "DivisionCreateModel",
    "DivisionEditModel",
    "FlagCreateModel",
    "FlagInfoModel",
    "GameInfoModel",
    "GameNoticeModel",
    "PostEditModel",
    # game
    "BasicGameInfoModel",
    "BasicWriteupInfoModel",
    "ChallengeDetailModel",
    "ChallengeInfo",
    "ChallengeTrafficModel",
    "CheatInfoModel",
    "ClientFlagContext",
    "ContainerInfoModel",
    "DetailedGameInfoModel",
    "FileRecord",
    "FlagSubmitModel",
    "GameDetailModel",
    "GameEvent",
    "GameJoinCheckInfoModel",
    "GameJoinModel",
    "GameNotice",
    "ParticipationModel",
    "ScoreboardModel",
    "Submission",
    "TeamModel",
    "TeamTrafficModel",
    # info
    "ClientCaptchaInfoModel",
    "ClientConfig",
    "PostDetailModel",
    "PostInfoModel",
    "SignatureVerifyModel",
    "TeamInfoModel",
    "TeamTransferModel",
    "TeamUpdateModel",
    "TeamUserInfoModel",
]
