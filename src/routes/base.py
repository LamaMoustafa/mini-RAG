from fastapi import FastAPI, APIRouter, Depends
from ..helpers.config import get_settings, Settings
base_router = APIRouter(
    prefix='/api/v1',
    tags=['api-v1']
)

@base_router.get('/')
async def welcome(app_settings:Settings = Depends(get_settings)):
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    file_allowed_type = app_settings.FILE_ALLOWED_TYPES
    return {
        'APP_NAME' : app_name,
        'APP_VERSION':app_version,
        'file_allowed_type':file_allowed_type
    }