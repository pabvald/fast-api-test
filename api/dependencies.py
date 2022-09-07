# Local Dependencies
# ------------------
from database import SessionLocal



# Dependencies 
# ------------
def get_db():
    """Obtains the database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()