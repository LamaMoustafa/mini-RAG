from fastapi import FastAPI, APIRouter, Depends, UploadFile, File, status, Request
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController, ProcessController
import os
import aiofiles
from models import ResponseSignal 
import logging
from .schemas.data import ProcessRequest

logger = logging.getLogger('uvicorn:error')

data_router = APIRouter(
    prefix='/api/v1/data',
    tags=['api-v1','data']
)

@data_router.post('/upload/{project_id}')
async def upload_data(project_id:str, file: UploadFile = File(...), 
                      app_settings:Settings = Depends(get_settings)):
    data_controller = DataController()
    #validate file properties
    is_valid, result_signal = data_controller.validate_uploaded_file(file= file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal" : result_signal
            }
        )

    file_path, file_id = data_controller.generate_unique_file_path(file_name=file.filename, project_id=project_id)
    # Log the file path for debugging
    print(f"Uploading file to: {file_path}")

    try:
        async with aiofiles.open(file_path, 'wb') as buffer:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await buffer.write(chunk)
            
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "signal" : ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )
    
    return JSONResponse(
                content={
                    "signal" : ResponseSignal.FILE_UPLOAD_SUCCESS.value,
                    "file_id" : file_id
                }
            ) 
    

@data_router.post('/process/{project_id}')
async def process_endpoint(project_id: str, ProcessRequest: ProcessRequest):

    file_id = ProcessRequest.file_id
    chunk_size = ProcessRequest.chunk_size
    overlap_size = ProcessRequest.overlap_size
    
    process_controller = ProcessController(project_id=project_id)
    
    file_content=process_controller.get_file_content(file_id=file_id)
    file_chunks=process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        overlap_size=overlap_size
    )
    
    if file_chunks is None or len(file_chunks)==0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal" : ResponseSignal.PROCESSING_FAILED.value
            }
        )
    
    return file_chunks