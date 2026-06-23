"""Data models for the Game API category.

Mirrors src/GZCTF/Models/Request/Game in the GZ::CTF source.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional

from .data import (
    Blood,
    DivisionInfo,
    DivisionItem,
    JoinedTeam,
    ScoreboardItem,
    TimeLineItem,
)
from .enum import (
    AnswerResult,
    ChallengeCategory,
    ChallengeType,
    ContainerStatus,
    EventType,
    NoticeType,
    ParticipationStatus,
    TimeStamp,
)


class BasicGameInfoModel(BaseModel):
    end: int
    id: int
    limit: int
    poster: Optional[str] = None
    start: int
    summary: str
    title: str


class BasicWriteupInfoModel(BaseModel):
    fileSize: int
    name: str
    note: str
    submitted: bool


class ChallengeDetailModel(BaseModel):
    attempts: int
    category: ChallengeCategory
    content: str
    context: ClientFlagContext
    deadline: Optional[int] = None
    hints: Optional[list[str]] = None
    id: int
    limit: int
    score: int
    title: str
    type: ChallengeType


class ChallengeInfo(BaseModel):
    bloods: list[Blood]
    category: ChallengeCategory
    deadline: Optional[int] = None
    disableBloodBonus: bool
    id: int
    score: int
    solved: int
    title: str = Field(min_length=1)


class ChallengeTrafficModel(BaseModel):
    category: ChallengeCategory
    count: int
    id: int
    isEnabled: bool
    title: str = Field(min_length=1)
    type: ChallengeType


class CheatInfoModel(BaseModel):
    ownedTeam: ParticipationModel
    submission: Submission
    submitTeam: ParticipationModel


class ClientFlagContext(BaseModel):
    closeTime: Optional[int] = None
    fileSize: Optional[int] = None
    instanceEntry: Optional[str] = None
    url: Optional[str] = None


class ContainerInfoModel(BaseModel):
    entry: str
    expectStopAt: int
    startedAt: int
    status: ContainerStatus


class DetailedGameInfoModel(BaseModel):
    content: str
    division: Optional[int] = None
    divisions: Optional[list[DivisionInfo]] = None
    end: int
    hidden: bool
    id: int
    inviteCodeRequired: bool
    limit: int
    poster: Optional[str] = None
    practiceMode: bool
    start: int
    status: ParticipationStatus
    summary: str
    teamCount: int
    teamName: Optional[str] = None
    title: str
    writeupRequired: bool


class FileRecord(BaseModel):
    fileName: str
    size: int
    updateTime: TimeStamp


class FlagSubmitModel(BaseModel):
    flag: str = Field(min_length=1)


class GameDetailModel(BaseModel):
    challengeCount: int
    challenges: dict[ChallengeCategory, list[ChallengeInfo]]
    rank: Optional[ScoreboardItem] = None
    teamToken: str = Field(min_length=1)
    writeupDeadline: int
    writeupRequired: bool


class GameEvent(BaseModel):
    team: str
    time: TimeStamp
    type: EventType
    user: str
    values: list[str]


class GameJoinCheckInfoModel(BaseModel):
    joinableDivisions: list[int]
    joinedTeams: list[JoinedTeam]


class GameJoinModel(BaseModel):
    divisionId: Optional[int] = None
    inviteCode: Optional[str] = None
    teamId: int


class GameNotice(BaseModel):
    """Game notice returned by the edit and game notice endpoints.

    Mirrors ``GameNotice`` in ``src/GZCTF/Models/Data/GameNotice.cs`` (which extends
    ``FormattableData<NoticeType>``). ``gameId`` and ``game`` are ``[JsonIgnore]`` in
    the source and are therefore not serialized.
    """

    id: int
    type: NoticeType
    values: Optional[list[str]] = None
    time: Optional[int] = None


class ParticipationModel(BaseModel):
    division: Optional[str] = None
    divisionId: Optional[int] = None
    id: int
    status: ParticipationStatus
    team: TeamModel


class ScoreboardModel(BaseModel):
    bloodBonus: int
    challengeCount: int
    challenges: dict[ChallengeCategory, list[ChallengeInfo]]
    divisions: list[DivisionItem]
    items: list[ScoreboardItem]
    timelines: list[TimeLineItem]
    updateTimeUtc: int


class Submission(BaseModel):
    answer: str = Field(max_length=127)
    challenge: str
    status: AnswerResult
    team: str
    time: int
    user: str


class TeamModel(BaseModel):
    avatar: Optional[str] = None
    id: int
    name: str


class TeamTrafficModel(BaseModel):
    avatar: Optional[str] = None
    count: int
    division: Optional[str] = None
    id: int
    name: Optional[str] = None
    teamId: int
