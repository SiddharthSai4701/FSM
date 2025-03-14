from fastapi import APIRouter
from server.schemas import User

from server.database import (
    get_database
)

router = APIRouter()

@router.get("/data")
async def get_data(): 
    db = await get_database() 
    result = "some function"
    return result

