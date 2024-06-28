from repository import LogEntryRepo
from database import get_db_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Response, Depends, status
from schemas import LogEntrySchema, LogLevel, DefaultWebResponse


router = APIRouter(tags=["LogsRoutes"])


@router.post("/save-log-sync", responses={
    200: {"model": DefaultWebResponse},
    500: {"model": DefaultWebResponse},
})
async def save_log(
    response: Response,
    data: LogEntrySchema,
    session: AsyncSession = Depends(get_db_session),
):
    err = await LogEntryRepo.save_log(session, data)
    if err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return DefaultWebResponse(status=LogLevel.ERROR, message=err)
    
    response.status_code = status.HTTP_200_OK
    return DefaultWebResponse(status=LogLevel.SUCCESS, message="log saved")
    
