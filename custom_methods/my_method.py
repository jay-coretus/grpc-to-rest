import json
from icecream import ic
import os
from fastapi import Response, Request
from google.protobuf.json_format import MessageToDict, MessageToJson
import json
import os
from fastapi import Response
from google.protobuf.json_format import MessageToJson

def my_method(request, request_data):
    ic(request, request_data)
    # for header_name, header_value in request.headers.items():
    #     ic(header_name, header_value)
    ic("This is supposed to run before grpc method call")
    # Modify the password in request_data
    request_data["password"] = "Password@123"


ENVIRONMENT = "development"

def _set_cookie(response, name, value, max_age=None):
    secure = ENVIRONMENT != "development"
    same_site = "none" if ENVIRONMENT != "development" else "lax"
    response.set_cookie(
        key=name,
        value=value,
        httponly=True,
        secure=secure,
        samesite=same_site,
        path="/",
        max_age=max_age,
        domain=f'.{os.getenv("WEB_URL", "leobrain.com")}',
    )

def set_cookies(grpc_response, call_details):
    # Create a Response object with the gRPC response as JSON
    response = Response(
        content=MessageToJson(grpc_response), 
        media_type="application/json"
    )
    # Set your cookies here
    cookies = {
        "session_id": "NjhiNzRhNDEtOWM5My00ZDc4LTk3MWUtNWNjNDFmZTM1ZWQ1",
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dXIiOiI2OGI3NGE0MS05YzkzLTRkNzgtOTcxZS01Y2M0MWZlMzVlZDUiLCJleHAiOjE3NDM3NjE4MTQsImlhdCI6MTc0MzE1NzAxNH0.quq-tGZJ_V7PuivNFl_cDZPZICR66Yg2UCgoMEKmibc",
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dXIiOiI2OGI3NGE0MS05YzkzLTRkNzgtOTcxZS01Y2M0MWZlMzVlZDUiLCJleHAiOjE3NDM3NjE4MTQsImlhdCI6MTc0MzE1NzAxNH0.quq-tGZJ_V7PuivNFl_cDZPZICR66Yg2UCgoMEKmibc",
    }
    for key, value in cookies.items():
        _set_cookie(response, key, value, max_age=36000)
    
    # Set CORS and expose cookie headers as needed
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Expose-Headers"] = "Set-Cookie"
    
    return response
