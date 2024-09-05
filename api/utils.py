from fastapi import Header, HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
import yaml

# read the tokens from the config file
with open("api/config/api_key.yaml", "r") as f:
    config = yaml.safe_load(f)

VALID_TOKENS = config["api_key"]
api_key = APIKeyHeader(name="X-Access-Token", scheme_name="X-Access-Token", auto_error=False)


def validate_token(x_access_token: str = Security(api_key)):
    if x_access_token == VALID_TOKENS:
        return x_access_token
    elif x_access_token is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Did not receive any access_token!")
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")