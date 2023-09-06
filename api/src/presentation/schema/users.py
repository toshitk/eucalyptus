from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Alice")
    email: str = Field(..., example="alice@example.com")

    class Config:
        orm_mode = True
