from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="John Smith")
    email: str = Field(..., example="sample@example.com")

    class Config:
        orm_mode = True
