from pydantic import BaseModel, PositiveFloat, validator, Field
class PredictionRequest(BaseModel):
    sepal_length: float = Field(default=1.0, description='Length of sepal')
    sepal_width: float = Field(default=1.0, description='Width of sepal')
    petal_length: float = Field(default=1.0, description='Length of petal')
    petal_width: float = Field(default=1.0, description='Width of petal')

    @validator('sepal_length', 'sepal_width', 'petal_length', 'petal_width', pre=True, always=True)
    def validate_float(cls, v):
        if v <= 0:
            raise ValueError('🤥 must be a positive number')
        return v