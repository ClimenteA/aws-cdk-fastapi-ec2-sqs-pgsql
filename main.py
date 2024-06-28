from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from router_logs import router as logs_api_router
from multiprocessing import cpu_count
from config import cfg


app = FastAPI(
    title="LogsAPI",
    description="Save/Retrieve log messages in mass.",
)


app.include_router(logs_api_router, prefix="/v1")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[url.strip() for url in cfg.ALLOWED_ORIGINS.split(" ") if url],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "OPTIONS", "DELETE"],
)


@app.middleware("http")
async def security_headers(request: Request, call_next):
    response: Response = await call_next(request)
    response.headers["strict-transport-security"] = (
        "max-age=63072000; includeSubdomains; preload"
    )
    response.headers["x-frame-options"] = "SAMEORIGIN"
    response.headers["x-content-type-options"] = "nosniff"
    response.headers["x-xss-protection"] = "0"
    response.headers["referrer-policy"] = "no-referrer, strict-origin-when-cross-origin"
    return response


if __name__ == "__main__":
    import uvicorn
    import alembic.config

    alembic_args = ["--raiseerr", "upgrade", "head"]
    alembic.config.main(argv=alembic_args)

    uvicorn.run(
        app="main:app",
        host=cfg.HOST,
        port=cfg.PORT,
        reload=cfg.DEBUG,
        proxy_headers=True,
        forwarded_allow_ips="*",
        workers=None if cfg.DEBUG else cpu_count(),
    )
