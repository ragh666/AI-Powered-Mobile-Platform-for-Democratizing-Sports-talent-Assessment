from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import SessionLocal
from app.models.athlete import Athlete, athlete_sport_association
from app.models.sport import Sport
from app.utils.auth import verify_token
from app.models.user import User
MAX_SPORTS_PER_ATHLETE = 3
router = APIRouter(prefix="/sport", tags=["sport"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# ------------------------
# Database Dependency
# ------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------------
# Get current user from JWT
# ------------------------
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload.get("user_id")


# ------------------------
# Get all available sports
# ------------------------
@router.get("/available")
def get_available_sports(db: Session = Depends(get_db)):
    sports = db.query(Sport).all()
    return [
        {"sport_id": sport.sport_id, "sport_name": sport.sport_name}
        for sport in sports
    ]


# ------------------------
# Add sport to athlete
# ------------------------
@router.post("/add/{sport_id}")
def add_sport_to_athlete(
    sport_id: int,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    athlete = db.query(Athlete).filter(Athlete.user_id == user_id).first()
    sport = db.query(Sport).filter(Sport.sport_id == sport_id).first()

    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete profile not found")
    if not sport:
        raise HTTPException(status_code=404, detail="Sport not found")

    # Check if already added
    stmt = select(athlete_sport_association).where(
        athlete_sport_association.c.athlete_id == athlete.user_id,
        athlete_sport_association.c.sport_id == sport.sport_id
    )
    if db.execute(stmt).first():
        raise HTTPException(status_code=400, detail="Sport already added")

    db.execute(
        athlete_sport_association.insert().values(
            athlete_id=athlete.user_id,
            sport_id=sport.sport_id
        )
    )
    db.commit()

    return {"message": f"{sport.sport_name} added successfully"}

@router.post("/athlete/{sport_id}")
def add_sport_to_athlete(
    sport_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    athlete = db.query(Athlete).filter(Athlete.user_id == current_user.id).first()
    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Athlete profile not found"
        )

    if len(athlete.sports) >= MAX_SPORTS_PER_ATHLETE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Maximum {MAX_SPORTS_PER_ATHLETE} sports allowed"
        )

    sport = db.query(Sport).filter(Sport.sport_id == sport_id).first()
    if not sport:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sport not found"
        )

    if sport in athlete.sports:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Sport already added"
        )

    athlete.sports.append(sport)
    db.commit()

    return {"message": "Sport added successfully"}
# ------------------------
# Remove sport from athlete
# ------------------------
@router.delete("/remove/{sport_id}")
def remove_sport_from_athlete(
    sport_id: int,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    athlete = db.query(Athlete).filter(Athlete.user_id == user_id).first()
    sport = db.query(Sport).filter(Sport.sport_id == sport_id).first()

    if not athlete or not sport:
        raise HTTPException(status_code=404, detail="Athlete or Sport not found")

    db.execute(
        athlete_sport_association.delete().where(
            athlete_sport_association.c.athlete_id == athlete.user_id,
            athlete_sport_association.c.sport_id == sport.sport_id
        )
    )
    db.commit()

    return {"message": f"{sport.sport_name} removed successfully"}


# ------------------------
# Get athlete's selected sports
# ------------------------
@router.get("/my-sports")
def get_my_sports(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    athlete = db.query(Athlete).filter(Athlete.user_id == user_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete profile not found")

    stmt = (
        select(Sport)
        .join(
            athlete_sport_association,
            Sport.sport_id == athlete_sport_association.c.sport_id
        )
        .where(athlete_sport_association.c.athlete_id == athlete.user_id)
    )

    sports = db.execute(stmt).scalars().all()
    return [
        {"sport_id": sport.sport_id, "sport_name": sport.sport_name}
        for sport in sports
    ]