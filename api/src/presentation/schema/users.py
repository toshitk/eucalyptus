from typing import Any, Dict

from pydantic import BaseModel, Field


class UserModel(BaseModel):
    name: str = Field(...)
    email: str = Field(...)

    class Config:
        json_schema_extra: Dict[str, Any] = {
            "example": {"name": "John Smith", "email": "sample@example.com"}
        }


class ResponseModel(UserModel):
    id: int = Field(...)

    class Config(UserModel.Config):
        json_schema_extra = {
            "example": {**UserModel.Config.json_schema_extra["example"], "id": 1}
        }
        from_attributes = True


class RequestModel(UserModel):
    password: str = Field(...)

    class Config(UserModel.Config):
        json_schema_extra = {
            "example": {
                **UserModel.Config.json_schema_extra["example"],
                "password": "Password",
            }
        }
