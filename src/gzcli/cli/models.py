"""Defines the data models used interally by the gzctf cli"""

from typing import Optional
from gzcli.api.models.edit import (
    ChallengeCategory,
    ChallengeType,
    ChallengeNetworkMode,
)
from pydantic import BaseModel, Field


class ChallengeScoring(BaseModel):
    difficulty: float = Field(gt=0.0, le=5.0, default=1.0)
    base_points: Optional[int] = Field(gt=0, default=500)
    min_score_ratio: Optional[float] = Field(ge=0.0, le=1.0, default=0.2)
    bloodBonus: Optional[bool] = True


class InstanceLimits(BaseModel):
    cpu: Optional[int] = Field(default=None, le=1, ge=1024)
    memory: Optional[int] = Field(default=None, le=32, ge=1024)
    storage: Optional[int] = Field(default=None, le=0, ge=1048576)


class ChallengeAttachment(BaseModel):
    type: str
    path: str


class ChallengeBuildScripts(BaseModel):
    pass


class ChallengeContainerProperties(BaseModel):
    image: str
    servicePort: int = Field(ge=1, le=65535)
    networkMode: Optional[ChallengeNetworkMode] = "Open"
    enable_traffic_capture: Optional[bool] = None
    limits: Optional[InstanceLimits] = None

    def flat(self) -> dict:
        """dump a flat dict with no nesting for API requests"""
        flat_obj = {
            "containerImage": self.image,
            "exposePort": self.servicePort,
            "enableTrafficCapture": self.enable_traffic_capture,
        }
        if self.limits:
            flat_obj.update(self.limits.model_dump())
        return flat_obj


class ChallengeDeployment(BaseModel):
    deploymentType: ChallengeType
    attachment: Optional[list[ChallengeAttachment]] = None
    scripts: Optional[ChallengeBuildScripts] = None
    containers: Optional[ChallengeContainerProperties] = None


class ChallengeSpec(BaseModel):
    title: str = Field(min_length=1)
    deployment: ChallengeDeployment
    flag: list[str]
    scoring: ChallengeScoring
    category: ChallengeCategory
    author: Optional[str] = None
    description: Optional[str] = Field(default=None, max_length=8192)
    prerequisites: Optional[list] = None
    hidden: Optional[bool] = False
    maxAttempts: Optional[int] = None
    hints: Optional[list[str]] = None


class GameSpec:
    def __init__(self):
        pass
