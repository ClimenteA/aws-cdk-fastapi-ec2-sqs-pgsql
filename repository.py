import models
from logger import log
from schemas import LogEntrySchema
from sqlalchemy.ext.asyncio import AsyncSession
    

class LogEntryRepo:

    @staticmethod
    async def save_log(db: AsyncSession, data: LogEntrySchema):
        try:
            db_log_entry = models.LogEntryModel(**data.model_dump())
            db.add(db_log_entry)
            await db.commit()
            await db.refresh(db_log_entry)
            return None
        except Exception as err:
            log.exception(err)
            return "failed to save log"
