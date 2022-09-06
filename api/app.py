# Base Dependencies 
# -----------------
from typing import Optional 

# FastAPI Dependencies
# --------------------
from uuid import UUID
from fastapi import FastAPI

# 3rd-party Dependencies
# ----------------------


# Local Dependencies
# ------------------
from models.user import UserBase
from models.tv_show import TVShow


tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with users.",
    }
]


app = FastAPI(openapi_tags=tags_metadata)


# Root 
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Users
@app.get("/users/", tags=['Users'])
def list_users(favorite_tv_show: Optional[str] = None):
    return [("User 1", TVShow("breaking_bad")), ("User 2", TVShow("breaking_bad"))]


@app.get("/users/{user_id}", tags=['Users'])
def show_user(user_id: UUID):
    return ("User", TVShow("the_wire"))
