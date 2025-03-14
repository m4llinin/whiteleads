from fastapi import (
    APIRouter,
    status,
    HTTPException,
    Request,
)

from src.api.dependencies import (
    VacancyUOWDep,
    AuthDep,
)
from src.services.vacancy import VacancyService
from src.schemes.vacancy import (
    VacancyScheme,
    VacancyInScheme,
)

router = APIRouter(
    prefix="/api/v1/vacancy",
    tags=["Vacancy"],
    dependencies=[AuthDep],
)


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_vacancy(uow: VacancyUOWDep, vacancy: VacancyInScheme):
    try:
        response = await VacancyService(uow).create_vacancy(vacancy.vacancy_id)
        return response
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.patch("/update")
async def update_vacancy(vacancy: VacancyInScheme, uow: VacancyUOWDep):
    try:
        response = await VacancyService(uow).update_vacancy(vacancy.vacancy_id)
        return response
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@router.get("/get/{vacancy_id}", response_model=VacancyScheme | None)
async def get_vacancy(uow: VacancyUOWDep, vacancy_id: str):
    return await VacancyService(uow).get_vacancy(vacancy_id)


@router.delete("/delete/{vacancy_id}")
async def delete_vacancy(vacancy_id: str, uow: VacancyUOWDep):
    try:
        response = await VacancyService(uow).delete_vacancy(vacancy_id)
        return response
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
        )
