from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    image_url: str
    title: str
    url: str
    description: str
    datetime: str
    type: Optional[str] = ""


class PostOut(PostBase):
    id: int
