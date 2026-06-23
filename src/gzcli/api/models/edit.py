"""Data models for the Edit API category.

Mirrors src/GZCTF/Models/Request/Edit in the GZ::CTF source.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Optional

from .data import Attachment, BloodBonus
from .enum import (
    ChallengeCategory,
    ChallengeNetworkMode,
    ChallengeType,
    FileType,
    GamePermission,
)
from .game import ContainerInfoModel


class AttachmentCreateModel(BaseModel):
    attachmentType: FileType
    fileHash: Optional[str] = None
    remoteUrl: Optional[str] = None


class ChallengeEditDetailModel(BaseModel):
    acceptedCount: int
    attachment: Optional[Attachment] = None
    category: ChallengeCategory
    containerImage: str  # this will be "" if challenge is not using containers, so no min_length=1 as suggested in doc
    content: str
    cpuCount: Optional[int] = Field(default=None, ge=1, le=1024)
    deadlineUtc: Optional[int] = None
    difficulty: float
    disableBloodBonus: Optional[bool] = None
    enableTrafficCapture: Optional[bool] = None
    exposePort: Optional[int] = None
    fileName: Optional[str] = None
    flags: list[FlagInfoModel]
    flagTemplate: Optional[str] = Field(default=None, max_length=120)
    hints: list[str]
    id: int
    isEnabled: bool
    memoryLimit: Optional[int] = Field(default=None, ge=32, le=1048576)
    minScoreRate: float = Field(ge=0.0, le=1.0)
    networkMode: ChallengeNetworkMode = "Open"
    originalScore: int
    storageLimit: Optional[int] = Field(default=None, ge=0, le=1048576)
    submissionLimit: int
    testContainer: Optional[ContainerInfoModel] = None
    title: str = Field(min_length=1)
    type: ChallengeType


class ChallengeInfoModel(BaseModel):
    category: ChallengeCategory
    deadlineUtc: Optional[int] = None
    id: Optional[int] = None
    isEnabled: Optional[bool] = None
    minScore: Optional[int] = None
    originalScore: Optional[int] = None
    score: Optional[int] = None
    title: str = Field(min_length=1)
    type: ChallengeType


class ChallengeUpdateModel(BaseModel):
    category: Optional[ChallengeCategory] = None
    containerImage: Optional[str] = None
    content: Optional[str] = None
    cpuCount: Optional[int] = Field(default=None, ge=1, le=1024)
    deadlineUtc: Optional[int] = None
    difficulty: Optional[float] = None
    disableBloodBonus: bool = False
    enableTrafficCapture: Optional[bool] = None
    exposePort: Optional[int] = None
    fileName: Optional[str] = None
    flagTemplate: Optional[str] = Field(default=None, max_length=120)
    hints: Optional[list[str]] = None
    isEnabled: Optional[bool] = None
    memoryLimit: Optional[int] = Field(default=None, ge=32, le=1048576)
    minScoreRate: Optional[float] = Field(default=None, ge=0.0, le=1.0)
    networkMode: Optional[ChallengeNetworkMode] = None
    originalScore: Optional[int] = None
    storageLimit: Optional[int] = Field(default=None, ge=0, le=1048576)
    submissionLimit: Optional[int] = Field(default=None, ge=0, le=10000)
    testContainer: Optional[ContainerInfoModel] = None
    title: Optional[str] = Field(default=None, min_length=1)
    type: Optional[ChallengeType] = None


class DivisionChallengeConfigModel(BaseModel):
    challengeId: int
    permissions: GamePermission


class DivisionCreateModel(BaseModel):
    challengeConfigs: Optional[list[DivisionChallengeConfigModel]] = None
    defaultPermissions: Optional[GamePermission] = None
    inviteCode: Optional[str] = Field(default=None, max_length=32)
    name: str = Field(min_length=1, max_length=31)


class DivisionEditModel(BaseModel):
    challengeConfigs: Optional[list[DivisionChallengeConfigModel]] = None
    defaultPermissions: Optional[GamePermission] = None
    inviteCode: Optional[str] = Field(default=None, max_length=32)
    name: Optional[str] = Field(default=None, min_length=1, max_length=31)


class FlagCreateModel(BaseModel):
    attachmentType: Optional[FileType] = None
    fileHash: Optional[str] = None
    flag: str = Field(min_length=1, max_length=127)
    remoteUrl: Optional[str] = None


class FlagInfoModel(BaseModel):
    attachment: Optional[Attachment] = None
    flag: str
    id: int


class GameInfoModel(BaseModel):
    acceptWithoutReview: bool
    bloodBonus: int = BloodBonus.DEFAULT  # packed first/second/third blood bonus
    containerCountLimit: int
    content: str
    end: int
    hidden: bool
    id: int
    inviteCode: Optional[str] = Field(default=None, max_length=32)
    poster: Optional[str] = None
    practiceMode: bool
    publicKey: str
    start: int
    summary: str
    teamMemberCountLimit: int
    title: str = Field(min_length=1)
    writeupDeadline: int
    writeupNote: str
    writeupRequired: bool

    @field_validator("bloodBonus", mode="before")
    @classmethod
    def _pack_blood_bonus(cls, value):
        """Allow bloodBonus to be supplied as a (first, second, third) percentage tuple."""
        if isinstance(value, (tuple, list)):
            if len(value) != 3:
                raise ValueError(
                    "bloodBonus tuple must have exactly 3 values (first, second, third)"
                )
            return BloodBonus.from_factors(*value)
        return value


class GameNoticeModel(BaseModel):
    content: str = Field(min_length=1)


class PostEditModel(BaseModel):
    content: Optional[str] = None
    isPinned: Optional[bool] = None
    summary: Optional[str] = None
    tags: Optional[list[str]] = None
    title: Optional[str] = Field(default=None, max_length=50)
