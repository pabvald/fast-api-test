# 3rd-party Dependencies
# -----------------------
from pydantic import BaseModel


class Message(BaseModel):
    message: str
