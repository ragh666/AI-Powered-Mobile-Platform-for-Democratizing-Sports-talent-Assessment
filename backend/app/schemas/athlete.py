from pydantic import BaseModel, Field, validator
from typing import Optional


from pydantic import BaseModel

class AthleteCreate(BaseModel):
    name: str
    age: int
    gender: str
    height_cm: float  # in cm
    weight_kg: float  # in kg
    fitness_level: str

    @validator("gender")
    def validate_gender(cls, v):
        if v.lower() not in ["male", "female", "other"]:
            raise ValueError("Gender must be male, female, or other")
        return v