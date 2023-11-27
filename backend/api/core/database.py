from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from api.env import SQLALCHEMY_DATABASE_URL, SQLALCHEMY_ASYNC_DATABASE_URL

# 同期エンジン（Alembic用）
sync_engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 非同期エンジン（FastAPI用）
async_engine = create_async_engine(SQLALCHEMY_ASYNC_DATABASE_URL, echo=True)
async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

Base = declarative_base()

async def get_db():
    try:
        db = async_session()
        yield db
    finally:
        if db:
            await db.close()