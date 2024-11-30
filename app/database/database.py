from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import  AsyncAttrs, AsyncSession
from sqlalchemy.orm import DeclarativeBase, declared_attr
from fastapi import Depends
import ssl
import asyncpg

from app.config.db import get_db_url



ssl_object = ssl.create_default_context()
ssl_object.check_hostname = False
ssl_object.verify_mode = ssl.CERT_NONE

DATABASE_URL =  get_db_url()
engine = create_async_engine(DATABASE_URL)
# engine = asyncpg.create_pool(DATABASE_URL, ssl=ssl_object)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# class get_session():
#     def __init__(self):
#         self.url = DATABASE_URL
        
#     async def __aenter__(self):
#         self.pool = await asyncpg.create_pool(self.url, ssl=ssl_object)
#         return self.pool

#     async def __aexit__(self, exc_type, exc, tb):
#         await self.pool.close()



class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"