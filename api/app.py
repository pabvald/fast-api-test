# Base Dependencies
# -----------------
from typing import Optional

# FastAPI Dependencies
# --------------------
from uuid import UUID
from fastapi import Depends, FastAPI, HTTPException

# 3rd-party Dependencies
# ----------------------
from sqlalchemy.orm import Session

# Local Dependencies
# ------------------
from crud import users
from database import engine, Base, get_db
from models.user import UserCreate, UserUpdate, User
from models.tv_show import TVShow


tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with users.",
    }
]

# create DB tables
Base.metadata.create_all(bind=engine)

# create app
app = FastAPI(openapi_tags=tags_metadata)


# -- Root --
@app.get("/")
async def root():
    return {"message": "Hello World"}


# -- Users --
@app.get("/users/", tags=["Users"], response_model=list[User])
def list_users(
    favorite_tv_show: Optional[TVShow] = None, db: Session = Depends(get_db)
):
    if favorite_tv_show:
        return users.get_user_by_tv_show(db, favorite_tv_show)
    else:
        return users.get_users(db)


@app.get("/user/{user_id}", tags=["Users"], response_model=User)
def show_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = users.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/user/", response_model=User)
def create_user(user: UserCreate = Depends(), db: Session = Depends(get_db)):
    return users.create_user(db=db, user=user)


@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = users.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return users.delete_user(db=db, user_id=user_id)


@app.put("/user/", response_model=User)
def update_user(user: UserUpdate = Depends(), db: Session = Depends(get_db)):
    db_user = users.get_user(db=db, user_id=user.id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return users.update_user(db=db, db_user=db_user, update_user=user)
