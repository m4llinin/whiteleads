from typing import Annotated
from datetime import datetime
from fastapi import (
    Header,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func


def _get_token(token: str = Header(alias="WWW-Authorization")) -> str:
    if "Bearer" not in token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    token.replace("Bearer ", "")
    return token


TokenDep = Annotated[str, Depends(_get_token)]
int_pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
int_not_null = Annotated[int, mapped_column(nullable=False)]
str_not_null = Annotated[str, mapped_column(nullable=False)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[
    datetime, mapped_column(server_default=func.now(), server_onupdate=func.now())
]
