from datetime import datetime

from pydantic import (
    BaseModel,
    field_validator,
)


class VacancyScheme(BaseModel):
    id: int
    vacancy_id: str
    vacancy_name: str
    description: str
    archived: bool
    company_name: str
    company_logo: str
    company_address: str
    vacancy_created_at: datetime

    @field_validator("vacancy_created_at")
    def remove_timezone(cls, v: datetime) -> datetime:
        if v.tzinfo is not None:
            return v.replace(tzinfo=None)
        return v


class VacancyInScheme(BaseModel):
    vacancy_id: str
