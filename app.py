from fastapi import FastAPI
import httpx
from dotenv import load_dotenv
import os

#app = FastAPI()
load_dotenv()

#@app.get("/")
#async def root():
#    return {"message": "Hello World"}


def foxproApi(options: dict):
    foxproApiUrl = os.getenv("FOXPRO_API_URL")
    foxproApiUser= os.getenv("FOXPRO_API_USER")
    foxproApiToken= os.getenv("FOXPRO_API_SECRET")
    foxproApiOriginUrl = os.getenv("FOXPRO_REQUEST_ORIGIN_URL")
    headers = {
        "Content-Type": "application/json",
        "Origin": foxproApiOriginUrl,
    }
    return httpx.get(foxproApiUrl, json = options, headers=headers, auth=(foxproApiUser, foxproApiToken))

response = foxproApi(options={
    'action':'GETINVSTOCK',
    'params': ['','','','S'],
    'keep_session': False,
})

print(response.json())
