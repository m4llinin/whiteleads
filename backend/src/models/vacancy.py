from datetime import datetime
from sqlalchemy.orm import Mapped

from src.core.database.base import Base
from src.core.dependencies import (
    str_not_null,
    int_pk,
)
from src.schemes.vacancy import VacancyScheme


class Vacancy(Base, scheme=VacancyScheme):
    __tablename__ = "vacancies"

    id: Mapped[int_pk]
    vacancy_id: Mapped[str_not_null]
    vacancy_name: Mapped[str_not_null]
    description: Mapped[str_not_null]
    archived: Mapped[bool]
    company_name: Mapped[str_not_null]
    company_logo: Mapped[str_not_null]
    company_address: Mapped[str_not_null]
    vacancy_created_at: Mapped[datetime]
