from src.core.database.base import SqlAlchemyRepository
from src.models.vacancy import Vacancy


class VacancyRepository(SqlAlchemyRepository, model=Vacancy):
    pass
