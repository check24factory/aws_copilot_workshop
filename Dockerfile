FROM python:3.12-slim-bullseye

COPY ./api/data_models ./api/data_models
COPY ./api/iris_model ./api/iris_model
COPY ./api/router ./api/router
COPY ./api/application.py ./api/application.py
COPY ./api/ModelLoader.py ./api/ModelLoader.py
COPY ./api/requirements.api.txt ./api/requirements.api.txt
COPY ./api/utils.py ./api/utils.py
COPY ./api/config ./api/config

RUN pip install --no-cache-dir -r api/requirements.api.txt

ENV UVICORN_HOST=0.0.0.0
ENV UVICORN_PORT=8000
ENV UVICORN_LOG_LEVEL=info
ENV PYTHONUNBUFFERED=1

EXPOSE ${UVICORN_PORT}
CMD uvicorn api.application:APP --host $UVICORN_HOST --port $UVICORN_PORT --log-level $UVICORN_LOG_LEVEL --workers 1 --timeout-keep-alive 10