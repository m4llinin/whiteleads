from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)

from src.core.utils.singleton import singleton


@singleton
class DBConnection:
    def __init__(self, url: str = None) -> None:
        self.url = url
        if self.url is None:
            raise ValueError("URL cannot be None")

        self._engine = create_async_engine(
            url,
            poolclass=NullPool,
        )
        self._async_sessionmaker = async_sessionmaker(
            self._engine,
            expire_on_commit=False,
        )

    def get_session(self) -> AsyncSession:
        return self._async_sessionmaker()
