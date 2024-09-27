from fastapi import Header, HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv
import os

load_dotenv()
VALID_TOKENS = os.getenv("API_KEY")
api_key = APIKeyHeader(name="X-Access-Token", scheme_name="X-Access-Token", auto_error=False)


def validate_token(x_access_token: str = Security(api_key)):
    if x_access_token == VALID_TOKENS:
        return x_access_token
    elif x_access_token is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Did not receive any access_token!")
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")