from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from api.router import predict, health

APP = FastAPI()

def custom_openapi():
    if APP.openapi_schema:
        return APP.openapi_schema
    openapi_schema = get_openapi(
        title="IRIS Species Prediction API 🌷",
        description="API predicts the species of the iris flower given its sepal and petal measurements.",
        version='1.0',
        routes=APP.routes,
    )
    APP.openapi_schema = openapi_schema
    return APP.openapi_schema


APP.openapi = custom_openapi

APP.include_router(predict.router, tags=['Operations'])
APP.include_router(health.router, tags=['Internal'])


@APP.get("/", tags=['Internal'])
async def docs_redirect():
    return RedirectResponse(url="/docs")
