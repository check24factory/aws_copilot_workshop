from pydantic import BaseModel, PositiveFloat, validator

class PredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    @validator('sepal_length', 'sepal_width', 'petal_length', 'petal_width', pre=True, always=True)
    def validate_float(cls, v):
        if v <= 0:
            raise ValueError('🤥 must be a positive number')
        return v