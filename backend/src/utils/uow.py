from src.core.utils.uow import UnitOfWork
from src.repositories.user import UserRepository
from src.repositories.vacancy import VacancyRepository


class AuthUOW(UnitOfWork):
    async def __aenter__(self):
        await super().__aenter__()
        self.users = UserRepository(self.session)


class VacancyUOW(UnitOfWork):
    async def __aenter__(self):
        await super().__aenter__()
        self.vacancies = VacancyRepository(self.session)
