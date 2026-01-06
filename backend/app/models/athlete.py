from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

athlete_sport_association = Table(
    "athlete_sport_association",
    Base.metadata,
    Column("athlete_id", Integer, ForeignKey("athletes.user_id"), primary_key=True),
    Column("sport_id", Integer, ForeignKey("sports.sport_id"), primary_key=True),
)

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class Athlete(Base):
    __tablename__ = "athletes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    height_cm= Column(Float, nullable=False)
    weight_kg = Column(Float, nullable=False)
    bmi = Column(Float, nullable=False)
    fitness_level = Column(String, nullable=False)

    sports = relationship(
        "Sport",
        secondary=athlete_sport_association,
        back_populates="athletes"
    )