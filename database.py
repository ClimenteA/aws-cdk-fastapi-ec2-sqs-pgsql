from collections.abc import AsyncGenerator

from sqlalchemy import exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config import cfg


Base = declarative_base()


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(cfg.DATABASE_URL)
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine)
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except exc.SQLAlchemyError:
            await session.rollback()
            raise
