import uvicorn
from fastapi import FastAPI

from recommendation_service.config import get_settings
from recommendation_service.health.router import router as health_router
from recommendation_service.logging import configure_logging


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(settings.log_level)

    app = FastAPI(
        title="Sloco Recommendation Service",
        version="0.1.0",
        docs_url="/v1/docs",
        openapi_url="/v1/openapi.json",
    )
    app.include_router(health_router, prefix="/v1")
    return app


app = create_app()


def run() -> None:
    settings = get_settings()
    uvicorn.run(
        "recommendation_service.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.app_env == "development",
        log_level=settings.log_level,
    )


if __name__ == "__main__":
    run()

