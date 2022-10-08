
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from async_generator import asynccontextmanager

ASYNC_SQLALCHEMY_DATABASE_URL = (
    "postgresql+asyncpg://postgres:postgres@db:5432/test_db"
)

async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)
Base = declarative_base()

@asynccontextmanager
async def get_async_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()


async def async_get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()
