from enum import Enum

from sqlalchemy import Enum as SqlEnum
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class CandidateStatus(str, Enum):
    APPLIED = "applied"
    INTERVIEW = "interview"
    SELECTED = "selected"
    REJECTED = "rejected"


class Candidate(Base):
    __tablename__ = "candidates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    skill: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[CandidateStatus] = mapped_column(
        SqlEnum(CandidateStatus),
        nullable=False,
        default=CandidateStatus.APPLIED,
    )
