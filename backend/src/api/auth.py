from fastapi import (
    APIRouter,
    status,
    HTTPException,
)

from src.api.dependencies import AuthUOWDep
from src.schemes.auth import (
    AuthSchemeIdResponse,
    AuthSchemeRequest,
    AuthSchemeResponse,
)
from src.services.auth import AuthService

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authorization"],
)


@router.post(
    "/signup",
    response_model=AuthSchemeIdResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(uow: AuthUOWDep, credentials: AuthSchemeRequest):
    try:
        user_id = await AuthService(uow).register_user(credentials)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return user_id


@router.post("/login", response_model=AuthSchemeResponse)
async def login(uow: AuthUOWDep, credentials: AuthSchemeRequest):
    try:
        tokens = await AuthService(uow).login_user(credentials)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return tokens


@router.post("/logout", response_model=AuthSchemeIdResponse)
async def logout(uow: AuthUOWDep, tokens: AuthSchemeResponse):
    try:
        user_id = await AuthService(uow).logout_user(tokens.access_token)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return user_id


@router.post("/refresh", response_model=AuthSchemeResponse)
async def refresh(uow: AuthUOWDep, tokens: AuthSchemeResponse):
    try:
        token = await AuthService(uow).refresh_token(tokens.refresh_token)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return token
