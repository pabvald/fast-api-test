# 3rd-party Dependencies
# ----------------------
from uuid import UUID
from sqlalchemy.orm import Session

# Local Dependencies
# ------------------
from models.tv_show import TVShow
from db_models.user import UserModel
from models.user import UserCreate, UserUpdate, User


def get_user(db: Session, user_id: UUID):
    return db.query(UserModel).filter(UserModel.id == user_id).first()
    

def get_user_by_name(db: Session, name: str):
    return db.query(UserModel).filter(UserModel.name == name).first()


def get_user_by_tv_show(db: Session, tv_show: TVShow):
    return db.query(UserModel).filter(UserModel.favorite_tv_show == tv_show).all()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()
    

def create_user(db: Session, user: UserCreate):
    # create user
    db_user = UserModel(name=user.name, favorite_tv_show=user.favorite_tv_show)
    # save to db
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
