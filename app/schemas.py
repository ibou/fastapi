from datetime import datetime
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
 

class PostCreate(PostBase):
    pass
    
class PostUpdate(PostBase):
     pass
   
class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    
    class Config:
        orm_mode = True
        
        
class UserCreate(BaseModel):
    email: str
    password: str
    
class UserOut(BaseModel):
    id: int
    email: str
    
    class Config:
        orm_mode = True
    
class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: int | None = None