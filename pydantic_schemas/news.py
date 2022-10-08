from pydantic import BaseModel
from datetime import datetime

class NewsBase(BaseModel):
    title: str
    full_text: str
    digest: str
    link: str
    post_date: str
    digest: str
    trend: str
    feature: str
    buh_likes: int | None
    buisness_likes: int | None

class NewsCreate(NewsBase):
    ...


class News(NewsBase):
    id: int

    class Config:
        orm_mode = True
