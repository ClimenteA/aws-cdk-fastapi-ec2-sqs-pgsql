from enum import StrEnum
from pydantic import BaseModel, Field


class LogLevel(StrEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"


class LogEntrySchema(BaseModel):
    level: LogLevel
    message: str = Field(max_length=5000)

    class Config:
        from_attributes = True


class DefaultWebResponse(BaseModel):
    status: str
    message: str