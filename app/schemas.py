from pydantic import BaseModel, ConfigDict, EmailStr

from .models import CandidateStatus


class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    skill: str
    status: CandidateStatus


class CandidateStatusUpdate(BaseModel):
    status: CandidateStatus


class CandidateRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    skill: str
    status: CandidateStatus
