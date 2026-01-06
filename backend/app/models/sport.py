from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.athlete import athlete_sport_association

class Sport(Base):
    __tablename__ = "sports"

    sport_id = Column(Integer, primary_key=True, index=True)
    sport_name = Column(String, unique=True, nullable=False)

    athletes = relationship(
        "Athlete",
        secondary=athlete_sport_association,
        back_populates="sports"
    )