from typing import Annotated
from fastapi import (
    Depends,
    status,
    HTTPException,
)

from src.core.dependencies import TokenDep
from src.services.auth import AuthService
from src.utils.uow import (
    AuthUOW,
    VacancyUOW,
)

AuthUOWDep = Annotated[AuthUOW, Depends(AuthUOW)]
VacancyUOWDep = Annotated[VacancyUOW, Depends(VacancyUOW)]


async def _is_auth(token: TokenDep, uow: AuthUOWDep):
    try:
        token = token.replace("Bearer ", "")
        if await AuthService(uow).check_is_auth(token):
            return True
        raise ValueError()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )


AuthDep = Depends(_is_auth)
