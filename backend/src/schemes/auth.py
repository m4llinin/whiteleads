from pydantic import BaseModel


class UserScheme(BaseModel):
    id: int
    login: str
    hashed_password: str
    is_active: bool


class AuthSchemeRequest(BaseModel):
    username: str
    password: str


class AuthSchemeResponse(BaseModel):
    access_token: str
    refresh_token: str | None = None


class AuthSchemeIdResponse(BaseModel):
    id: int
