from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse,Token,UserLogin
from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from fastapi.security import OAuth2PasswordBearer


router = APIRouter(prefix="/auth", tags=["Auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.get("/_swagger_auth_test")
def swagger_auth_test(token: str = Depends(oauth2_scheme)):
    return {"status": "ok"}
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(
        data={"sub": str(db_user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
class LoginSchema(BaseModel):
    username: str
    password: str

# ------------------------
# Login route
# ------------------------
@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    username = data.username
    password = data.password

    user = db.query(User).filter(User.email == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}   