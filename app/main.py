from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Candidate, CandidateStatus
from .schemas import CandidateCreate, CandidateRead, CandidateStatusUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Candidate Management API", version="1.0.0")


@app.get("/")
def root():
    return {
        "message": "Candidate Management API is running.",
        "docs": "/docs",
    }


@app.post("/candidates", response_model=CandidateRead, status_code=status.HTTP_201_CREATED)
def create_candidate(payload: CandidateCreate, db: Session = Depends(get_db)):
    candidate = Candidate(
        name=payload.name,
        email=str(payload.email),
        skill=payload.skill,
        status=payload.status,
    )
    db.add(candidate)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Candidate with this email already exists.",
        )

    db.refresh(candidate)
    return candidate


@app.get("/candidates", response_model=list[CandidateRead])
def get_candidates(
    status_filter: CandidateStatus | None = Query(default=None, alias="status"),
    db: Session = Depends(get_db),
):
    query = db.query(Candidate)
    if status_filter is not None:
        query = query.filter(Candidate.status == status_filter)
    return query.order_by(Candidate.id.asc()).all()


@app.put("/candidates/{candidate_id}/status", response_model=CandidateRead)
def update_candidate_status(
    candidate_id: int,
    payload: CandidateStatusUpdate,
    db: Session = Depends(get_db),
):
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if candidate is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Candidate not found.")

    candidate.status = payload.status
    db.commit()
    db.refresh(candidate)
    return candidate
