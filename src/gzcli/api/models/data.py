"""Data models for miscellaneous fields used in other data models but not as the whole
request and response body.

Simply put, the name of all classes here does not end with "Model"

(but there does exist request/response data models that does not end with "Model" such as `Submission` or `GameEvent`)

This behaviour does not necessarily mirror the GZ::CTF source.
"""

from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from .enum import FileType, GamePermission, SubmissionType


class ApiToken(BaseModel):
    createdAt: int
    creator: Optional[str] = None
    creatorId: str = Field(min_length=1)
    expiresAt: Optional[int] = None
    id: str
    isRevoked: bool
    lastUsedAt: Optional[int] = None
    name: str = Field(min_length=1, max_length=128)


class Attachment(BaseModel):
    fileSize: Optional[int] = None
    id: int
    type: FileType
    url: Optional[str] = None


class Blood(BaseModel):
    avatar: Optional[str] = None
    id: int
    name: str = Field(min_length=1)
    submitTimeUtc: Optional[int] = None


class BloodBonus:
    """First/second/third blood bonus packed into a single integer.

    Mirrors the ``BloodBonus`` struct in GZCTF.Utils (``src/GZCTF/Utils/Shared.cs``):
    three 10-bit fields holding the bonus in per-mille (percentage * 10), packed as
    ``(first << 20) | (second << 10) | third``. The default is 5% / 3% / 1%.
    """

    MASK = 0x3FF  # 10 bits per field
    MAX_PERMILLE = 1000  # logical max per field (100%)
    DEFAULT = (50 << 20) | (30 << 10) | 10  # 5% / 3% / 1% -> 52459530

    @classmethod
    def from_factors(
        cls, first: float = 5.0, second: float = 3.0, third: float = 1.0
    ) -> int:
        """Pack three blood-bonus percentages into the integer the API expects."""
        packed = 0
        for shift, percentage in ((20, first), (10, second), (0, third)):
            permille = round(percentage * 10)
            if not 0 <= permille <= cls.MAX_PERMILLE:
                raise ValueError(
                    f"blood bonus {percentage}% out of range (0% to 100%)"
                )
            packed |= permille << shift
        return packed

    @classmethod
    def to_factors(cls, value: int) -> tuple[float, float, float]:
        """Unpack a blood-bonus integer back into (first, second, third) percentages."""
        return (
            ((value >> 20) & cls.MASK) / 10,
            ((value >> 10) & cls.MASK) / 10,
            (value & cls.MASK) / 10,
        )


class ChallengeItem(BaseModel):
    id: int
    score: int
    time: int
    type: SubmissionType
    userName: Optional[str] = None


class DivisionChallengeItem(BaseModel):
    challengeId: int
    permissions: GamePermission


class DivisionInfo(BaseModel):
    id: int
    inviteCodeRequired: bool
    name: str


class DivisionItem(BaseModel):
    challengeConfigs: dict[str, DivisionChallengeItem]
    defaultPermissions: GamePermission
    id: int
    name: str = Field(min_length=1)


class JoinedTeam(BaseModel):
    division: int
    id: int


class RequestResponse(BaseModel):
    status: int
    title: str


class ScoreboardItem(BaseModel):
    avatar: Optional[str] = None
    bio: Optional[str] = None
    divisionId: Optional[int] = None
    divisionRank: Optional[int] = None
    id: int
    lastSubmissionTime: int
    name: str = Field(min_length=1)
    rank: int
    score: int
    solvedChallenges: list[ChallengeItem]
    solvedCount: int


class TimeLine(BaseModel):
    score: int
    time: int


class TimeLineItem(BaseModel):
    divisionId: int
    teams: list[TopTimeLine]


class TopTimeLine(BaseModel):
    id: int
    items: list[TimeLine]
    name: str = Field(min_length=1)
