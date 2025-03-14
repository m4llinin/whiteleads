from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.core.database.base import Base
from src.core.dependencies import (
    int_pk,
    str_not_null,
)

from src.schemes.auth import UserScheme


class User(Base, scheme=UserScheme):
    __tablename__ = "users"

    id: Mapped[int_pk]
    login: Mapped[str_not_null]
    hashed_password: Mapped[str_not_null]
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False)
