from api.repository import LogEntryRepo
from api.schemas import LogEntrySchema, LogLevel, DefaultWebResponse
from fastapi import APIRouter, Response, BackgroundTasks, status


router = APIRouter(tags=["LogsRoutes"])


@router.post("/save-log-sync", responses={
    200: {"model": DefaultWebResponse},
    500: {"model": DefaultWebResponse},
})
async def save_log(
    response: Response,
    data: LogEntrySchema,
    background_tasks: BackgroundTasks,
):
    background_tasks.add_task(LogEntryRepo.save_log, data)
    response.status_code = status.HTTP_200_OK
    return DefaultWebResponse(status=LogLevel.SUCCESS, message="log added in queue")
    
