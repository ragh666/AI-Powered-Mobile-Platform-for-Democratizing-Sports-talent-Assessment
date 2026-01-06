from app.database import Base, engine
from app.models import user, athlete, sport

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")