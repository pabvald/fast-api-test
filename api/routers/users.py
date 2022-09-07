# Base Dependencies
# -----------------
from typing import Optional

# FastAPI Dependencies
# --------------------
from uuid import UUID
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

# 3rd-party Dependencies
# ----------------------
from sqlalchemy.orm import Session

# Local Dependencies
# ------------------
from crud import users
from dependencies import get_db
from models.message import Message
from models.user import UserCreate, UserUpdate, User
from models.tv_show import TVShow


# UsersRouter
router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

# -- Users --
@router.get("/", response_model=list[User])
def list_users(
    favorite_tv_show: Optional[TVShow] = None, db: Session = Depends(get_db)
):
    if favorite_tv_show:
        response = users.get_users_by_tv_show(db, favorite_tv_show)
    else:
        response = users.get_users(db)

    return response


@router.get(
    "/{user_id}",
    response_model=User,
    responses={404: {"model": Message}},
)
def show_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = users.get_user(db=db, user_id=user_id)

    if db_user is None:
        return JSONResponse(status_code=404, content={"message": "User not found"})

    return db_user


@router.post("/", response_model=User)
def create_user(user: UserCreate = Depends(), db: Session = Depends(get_db)):
    return users.create_user(db=db, user=user)


@router.delete(
    "/{user_id}",
    response_model=User,
    responses={404: {"model": Message}},
)
def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = users.get_user(db=db, user_id=user_id)

    if db_user is None:
        return JSONResponse(status_code=404, content={"message": "User not found"})

    return users.delete_user(db=db, db_user=db_user)


@router.put("/{user_id}", response_model=User, responses={404: {"model": Message}})
def update_user(user_id: UUID, update_user: UserUpdate= Depends(), db: Session = Depends(get_db)):
    db_user = users.get_user(db=db, user_id=user_id)

    if db_user is None:
        return JSONResponse(status_code=404, content={"message": "User not found"})

    return users.update_user(db=db, db_user=db_user, update_user=update_user)
