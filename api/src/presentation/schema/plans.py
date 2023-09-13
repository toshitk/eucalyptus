from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="My Plan")

    class Config:
        orm_mode = True
