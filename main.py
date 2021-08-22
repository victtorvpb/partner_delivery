from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.core.schemas.messages import ResponseMessage
from configs.base import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/its-alive", response_model=ResponseMessage)
    async def its_alive():
        return {"status": "its_alive"}

    return app


app = create_app()
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG,
        reload=settings.DEBUG,
    )
