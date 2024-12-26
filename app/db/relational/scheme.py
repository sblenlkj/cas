from pydantic import BaseModel

class TgChannel(BaseModel):
    name: str
    link: str
