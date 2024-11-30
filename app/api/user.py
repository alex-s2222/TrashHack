from fastapi import APIRouter, Path, Depends
from sqlalchemy.future import select
from pydantic import create_model

from typing import Optional, Annotated
from app.service import user as db
from app.schemas import user as shemas



router = APIRouter()

@router.get("/users")
async def router_get_users(params: shemas.getUser = Depends(shemas.getUser.parser)):
    filters_params = {}
    for key, value in params.items():
        if value is not None:
            filters_params[key] = value

    users_data = await db.get_users(**filters_params)
    return users_data



@router.get("/users/{id}")
async def router_get_user(id: Optional[int] = Path(...)):
    user_data = await db.get_user(id)

    if user_data is None:
        return {"error": "User not found"}
    
    return {'id': user_data.__dict__}

