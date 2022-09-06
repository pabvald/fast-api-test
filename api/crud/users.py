# 3rd-party Dependencies
# ----------------------
from uuid import UUID
from sqlalchemy.orm import Session

# Local Dependencies
# ------------------
from models.tv_show import TVShow
from db_models.user import UserModel
from models.user import UserCreate, UserUpdate


def get_user(db: Session, user_id: UUID):
    """Gets a User by id"""
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    """Gets a User by name"""
    return db.query(UserModel).filter(UserModel.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Gets all users"""
    return db.query(UserModel).offset(skip).limit(limit).all()


def get_users_by_tv_show(db: Session, tv_show: TVShow, skip: int = 0, limit: int = 100):
    """Gets all users that watch a certain tv show"""
    return (
        db.query(UserModel)
        .filter(UserModel.favorite_tv_show == tv_show)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_user(db: Session, user: UserCreate):
    """Creates a new User"""
    # create user
    db_user = UserModel(name=user.name, favorite_tv_show=user.favorite_tv_show)
    # save to db
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, db_user: UserModel):
    """Deletes a User"""
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


def update_user(db: Session, db_user: UserModel, update_user: UserUpdate):
    """Modifies a User"""
    if db_user.id != update_user.id:
        raise Exception("the UserUpdate doesn't correspond to the queried User")

    if update_user.name:
        db_user.name = update_user.name
    if update_user.favorite_tv_show:
        db_user.favorite_tv_show = update_user.favorite_tv_show
    db.commit()

    return db_user
