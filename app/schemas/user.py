from pydantic import BaseModel, EmailStr
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreat(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_admin: bool

    class Config:
        fron_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"