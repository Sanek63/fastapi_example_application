import uvicorn

from app.server import app
from core.config import config


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config.APP_HOST,
        port=config.APP_PORT
    )
