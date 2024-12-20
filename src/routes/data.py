from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController

data_router = APIRouter(
    prefix='/api/v1/data',
    tags=['api-v1','data']
)

@data_router.post('/upload/{project_id}')
async def upload_data(project_id:str, file:UploadFile, 
                      app_settings:Settings = Depends(get_settings)):
    #validate file properties
    is_valid, result_signal = DataController().validate_uploaded_file(file= file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal" : result_signal
            }
        )
    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    