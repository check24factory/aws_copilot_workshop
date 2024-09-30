from api.data_models.v1.request import PredictionRequest
from api.data_models.v1.response import PredictionResponse
import pandas as pd
from api.ModelLoader import ModelLoader
from fastapi import APIRouter, HTTPException, Depends
from api.utils import validate_token

router = APIRouter()
iris_model = ModelLoader(model_path="api/iris_model")


@router.post("/classify_iris", response_model=PredictionResponse)
async def predict(request: PredictionRequest, token: str = Depends(validate_token)):
    try:
        print("Request: ", request)
        # Prepare data for prediction
        data = pd.DataFrame([{
            'sepal_length': request.sepal_length,
            'sepal_width': request.sepal_width,
            'petal_length': request.petal_length,
            'petal_width': request.petal_width
        }])

        # Make predictions
        predictions = iris_model.predict(data)

        print("Predictions: ", predictions)

        # Return predictions in response
        return PredictionResponse(predictions=predictions.tolist())

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))