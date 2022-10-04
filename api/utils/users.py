from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert
from db.models.user import User
from pydantic_schemas.user import UserCreate


async def get_user(db: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_users(db: AsyncSession):
    query = select(User)
    result = await db.execute(query)
    return result.scalars().all()


async def create_user(db: AsyncSession, user: UserCreate):
    db_user = insert(User).values(age=user.age, category=user.category, gender=user.gender)
    result = await db.execute(db_user)
    return result.first()

    # db_user = User(age=user.age, category=user.category, gender=user.gender)
    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)
    # return db_user