from api.database import Base
from sqlalchemy import Column, Integer, String, DateTime, func


class LogEntryModel(Base):
    
    __tablename__ = "log_entries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(5000))
    level = Column(String(50))
    timestamp = Column(DateTime, nullable=True, server_default=func.now())

    def __repr__(self) -> str:
        return f"Log(id={self.id!r}, message={self.message!r}, level={self.level!r}, timestamp={self.timestamp!r})"
