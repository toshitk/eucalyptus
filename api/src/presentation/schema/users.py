from pydantic import BaseModel, Field


class UserModel(BaseModel):
    name: str = Field(..., example="John Smith")
    email: str = Field(..., example="sample@example.com")


class ResponseModel(UserModel):
    id: int = Field(..., example=1)

    class Config:
        orm_mode = True


class RequestModel(UserModel):
    password: str = Field(..., example="Password")
