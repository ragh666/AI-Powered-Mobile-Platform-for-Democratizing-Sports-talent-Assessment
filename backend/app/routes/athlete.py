from app.utils.auth import verify_token
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.athlete import Athlete
from app.schemas.athlete import AthleteCreate
from app.utils.deps import get_current_user
from app.utils.bmi import calculate_bmi

router = APIRouter(
    prefix="/athlete",
    tags=["Athlete"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.athlete import Athlete
from app.schemas.athlete import AthleteCreate
from app.utils.deps import get_current_user
from app.utils.bmi import calculate_bmi

router = APIRouter(
    prefix="/athlete",
    tags=["Athlete"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", status_code=201)
def create_athlete(
    athlete: AthleteCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    existing = db.query(Athlete).filter(
        Athlete.user_id == current_user.id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Profile already exists")

    bmi_data = calculate_bmi(
        athlete.height_cm,
        athlete.weight_kg
    )

    new_athlete = Athlete(
        user_id=current_user.id,
        name=athlete.name,
        age=athlete.age,
        gender=athlete.gender,
        height_cm=athlete.height_cm,
        weight_kg=athlete.weight_kg,
        bmi=bmi_data["bmi"],
        fitness_level=athlete.fitness_level,
        location=athlete.location
    )

    db.add(new_athlete)
    db.commit()
    db.refresh(new_athlete)

    return {
        "message": "Athlete profile created",
        "bmi": bmi_data
    }

@router.get("/test")
def athlete_test():
    return {"status": "athlete router working"}
@router.get("/profile")
def get_athlete_profile(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    athlete = db.query(Athlete).filter(Athlete.user_id == user_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete profile not found")
    return athlete