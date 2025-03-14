from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import (
    FastAPI,
    APIRouter,
)
from fastapi.middleware.cors import CORSMiddleware

from .core.config import Config
from .core.database.connection import DBConnection
from .utils.api_hh import HHHandler

from .api.auth import router as auth_router
from .api.vacancy import router as vacancy_router


class App:
    routers: list[APIRouter] = [
        auth_router,
        vacancy_router,
    ]

    def __init__(self, config: Config) -> None:
        self._config = config

    def setup_cors(self, app: FastAPI) -> None:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[
                "http://localhost",
                "http://localhost:5173",
                "http://0.0.0.0:5173",
                "http://frontend:5173",
                "http://frontend:80",
            ],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["*"],
        )

    def include_routers(self, app: FastAPI) -> None:
        for router in self.routers:
            app.include_router(router)

    @asynccontextmanager
    async def lifespan(self, app: FastAPI) -> AsyncGenerator[None, None]:
        DBConnection(
            url=self._config.db.URL,
        )
        HHHandler(
            url="https://api.hh.ru",
        )
        yield

    def initialize(self) -> FastAPI:
        app = FastAPI(lifespan=self.lifespan)
        self.setup_cors(app)
        self.include_routers(app)
        return app


app = App(config=Config()).initialize()
