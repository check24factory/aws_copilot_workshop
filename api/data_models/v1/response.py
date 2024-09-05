from typing import List, Literal
from pydantic import BaseModel, Field


class PredictionResponse(BaseModel):
    predictions: List[Literal["Iris-setosa", "Iris-versicolor", "Iris-virginica"]]


class HealthResponse(BaseModel):
    """
    Health response data model
    """
    http_status_code: int = Field(None, example=200)
    health: str = Field(None, example="OK")
    environment: str = Field(None, example="prod")
    cpu_count: int = Field(None, example=4)
    cpu_usage_relative: str = Field(None, example="19.0%")
    memory_usage_relative: str = Field(None, example="59.6%")
    memory_usage_absolute: str = Field(None, example="16665Mb")
    disk_usage: str = Field(None, example="22.5%")
