from sqlalchemy.future import select
from sqlalchemy import and_
from sqlalchemy.orm import Query

from app.database.database import async_session
from app.models.user import User, Status


async def get_user(id: int):
    user_data = None
    async with async_session() as conn:
        stmt = Query(User, Status).outerjoin(Status, and_(User.id == Status.user_id)).where(User.id == id)
        result = await conn.execute(stmt)
        user_data = result.scalar_one_or_none()

    return user_data


async def get_users(**filters):
    user_data = None
    async with async_session() as conn:
        stmt = select(User).filter_by(**filters)
        result = await conn.execute(stmt)
        user_data = result.scalars()
    
    result = [data.__dict__ for data in user_data]
    return result
