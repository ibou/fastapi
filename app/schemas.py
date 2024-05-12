from pydantic import BaseModel, Field
from typing_extensions import Annotated
from datetime import datetime
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        # orm_mode = True
        from_attributes = True


class Post(PostBase):
    id: int
    owner_id: int
    owner: UserOut
    created_at: datetime

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
