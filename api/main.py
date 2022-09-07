# FastAPI Dependencies
# --------------------
from fastapi import Depends, FastAPI

# Local Dependencies
# ------------------
from crud import users
from database import engine, Base
from dependencies import get_db
from routers.users import router as UsersRouter


tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with users.",
    }
]

# create DB tables
Base.metadata.create_all(bind=engine)

# create app
app = FastAPI(openapi_tags=tags_metadata, dependencies=[Depends(get_db)])


# -- Root --
@app.get("/")
async def root():
    return {"message": "Hello World"}


# -- Users --
app.include_router(UsersRouter)
