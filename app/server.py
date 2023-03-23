from fastapi import FastAPI

from api import init_sub_applications


def create_app() -> FastAPI:
    app_ = FastAPI(
        title=f"calculator-service",
        description=f"Service API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    init_sub_applications(app_=app_)

    return app_


app = create_app()
