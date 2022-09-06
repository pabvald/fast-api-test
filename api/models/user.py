"""
    Pydantic Models for User
"""

# Base Dependencies 
# ----------------------
from typing import Optional
from uuid import UUID

# 3rd-party Dependencies
#-----------------------
from pydantic import BaseModel

# Local Dependencies
# ------------------
from .tv_show import TVShow


class UserBase(BaseModel):
    """ User model to create/read """
    name: str
    favorite_tv_show: TVShow


class UserCreate(UserBase):
    """ User model to create"""
    pass 


class UserUpdate(BaseModel):
    """ User model to update """
    id: UUID
    name: Optional[str]
    favorite_tv_show : Optional[TVShow]


class User(UserBase):
    """ User model for reading / returning"""
    id: UUID

    class Config:
        orm_mode = True
        use_enum_values = True

