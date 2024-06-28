from sqlalchemy.ext.asyncio import AsyncSession
from api.models import LogEntryModel
from api.logger import log
from api.schemas import LogEntrySchema
    

class LogEntryRepo:

    @staticmethod
    async def save_log(db: AsyncSession, data: LogEntrySchema):
        try:
            db_log_entry = LogEntryModel(**data.model_dump())
            db.add(db_log_entry)
            await db.commit()
            await db.refresh(db_log_entry)
            return None
        except Exception as err:
            log.exception(err)
            return "failed to save log"
