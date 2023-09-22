from typing import Any, Dict

from pydantic import BaseModel, Field


class PlanModel(BaseModel):
    name: str = Field(...)

    class Config:
        json_schema_extra: Dict[str, Any] = {"example": {"name": "My Plan"}}


class ResponseModel(PlanModel):
    id: int = Field(...)

    class Config(PlanModel.Config):
        json_schema_extra = {
            "example": {**PlanModel.Config.json_schema_extra["example"], "id": 1}
        }
        from_attributes = True


class RequestModel(PlanModel):
    class Config(PlanModel.Config):
        pass
