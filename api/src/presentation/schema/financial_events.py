from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    id: int = Field(...)
    plan_id: int = Field(...)
    type: int = Field(...)
    category: str = Field()
    name: str = Field(...)
    year: int = Field(...)
    month: int = Field(...)
    amount: int = Field()

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "plan_id": 1,
                "type": 1,
                "category": "salaly",
                "name": "monthly salary",
                "year": 2000,
                "month": 1,
                "amount": 500000,
            }
        }
        from_attributes = True
