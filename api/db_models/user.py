# Fast-API Dependencies
# ---------------------
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE

# 3rd-party Dependencies
# -----------------------
from sqlalchemy import Column, String, Enum

# Local Dependencie
# ------------------
from models.tv_show import TVShow
from database import Base


class UserModel(Base):
    """User DB model"""

    __tablename__ = "users"

    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String(50))
    favorite_tv_show = Column(Enum(TVShow))
