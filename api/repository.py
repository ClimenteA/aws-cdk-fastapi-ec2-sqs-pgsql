from api.models import LogEntryModel
from api.logger import log
from api.schemas import LogEntrySchema
from api.database import get_db_session 


class LogEntryRepo:

    @staticmethod
    async def save_log(data: LogEntrySchema):
        try:
            async with get_db_session() as db: 
                db_log_entry = LogEntryModel(**data.model_dump())
                db.add(db_log_entry)
                await db.commit()
                await db.refresh(db_log_entry)
            log.info(f"Saved {data}")
            return None
        except Exception as err:
            log.exception(err)
            return "failed to save log"
