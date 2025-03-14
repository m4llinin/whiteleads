from datetime import datetime

from src.utils.uow import VacancyUOW
from src.utils.api_hh import HHHandler


class VacancyService:
    def __init__(self, uow: VacancyUOW) -> None:
        self._uow = uow

    async def create_vacancy(self, vacancy_id: str) -> dict[str, str]:
        async with self._uow:
            if (
                await self._uow.vacancies.get_one(
                    {
                        "vacancy_id": vacancy_id,
                    },
                )
            ) is not None:
                raise ValueError(f"Vacancy with vacancy_id {vacancy_id} already exists")

            vacancy = await HHHandler().get_vacancy(vacancy_id=vacancy_id)
            if vacancy is None:
                raise ValueError(f"Error with request to https://api.hh.ru")

            vacancy.update(vacancy_id=vacancy_id)

            try:
                await self._uow.vacancies.insert(vacancy)
                await self._uow.commit()
                response = "ok"
            except Exception as e:
                response = "bad"

        return {
            "response": response,
        }

    async def update_vacancy(self, vacancy_id: str) -> dict[str, str]:
        async with self._uow:
            if (
                await self._uow.vacancies.get_one(
                    {
                        "vacancy_id": vacancy_id,
                    },
                )
            ) is None:
                raise ValueError(f"Vacancy: {vacancy_id} does not exist")

            vacancy = await HHHandler().get_vacancy(vacancy_id=vacancy_id)
            if vacancy is None:
                raise ValueError(f"Error with request to https://api.hh.ru")

            try:
                await self._uow.vacancies.update(
                    filters={
                        "vacancy_id": vacancy_id,
                    },
                    data=vacancy,
                )
                await self._uow.commit()
                response = "ok"
            except Exception:
                response = "bad"

        return {
            "response": response,
        }

    async def get_vacancy(self, vacancy_id: str) -> dict[str, str | datetime] | None:
        async with self._uow:
            return await self._uow.vacancies.get_one(
                {
                    "vacancy_id": vacancy_id,
                }
            )

    async def delete_vacancy(self, vacancy_id: str) -> dict[str, str]:
        async with self._uow:
            if (
                await self._uow.vacancies.get_one(
                    {
                        "vacancy_id": vacancy_id,
                    },
                )
            ) is None:
                raise ValueError(f"Vacancy: {vacancy_id} does not exist")

            try:
                await self._uow.vacancies.delete(
                    filters={
                        "vacancy_id": vacancy_id,
                    },
                )
                await self._uow.commit()
                response = "ok"
            except Exception:
                response = "bad"

        return {
            "response": response,
        }
