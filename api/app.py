# Base Dependencies 
# -----------------

# FastAPI Dependencies
# --------------------
from fastapi import FastAPI

# 3rd-party Dependencies
# ----------------------


# Local Dependencies
# ------------------



app = FastAPI()



# Root 
@app.get("/")
async def root():
    return {"message": "Hello World"}
