from fastapi import FastAPI
from app.routes import auth, athlete
from fastapi.security import OAuth2PasswordBearer
app = FastAPI(title="AI Sports Platform")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
app.include_router(auth.router)
app.include_router(athlete.router)

