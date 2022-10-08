from pydantic import BaseModel


class UserBase(BaseModel):
    category: str



class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
