import { useState } from 'react';
import { createVacancy, getVacancy } from '../../src/api/Vacancy';
import VacancyView from "../components/Vacancy/VacancyView";
import { useAuth } from '../context/AuthContext';

export default function Dashboard() {
    const { logout } = useAuth()
    const [getError, setGetError] = useState(false);
    const [createError, setCreateError] = useState(false);
    const [vacancyId, setVacancyId] = useState("0");
    const [vacancy, setVacancy] = useState()

    const createClick = async () => {
        try {
            const vacancy_response = await createVacancy(vacancyId)
            if (vacancy_response === undefined) {
                setCreateError(true)
                setTimeout(() => {
                    setCreateError(false);
                }, 1000);
                return
            }
            setVacancy(await getVacancy(vacancyId))
        }
        catch {
            setCreateError(true)
            setTimeout(() => {
                setCreateError(false);
            }, 1000);
        }
    }

    const getClick = async () => {
        try {
            const vacancy_response = await getVacancy(vacancyId)
            if (vacancy_response === undefined || vacancy_response === null) {
                setGetError(true)
                setTimeout(() => {
                    setGetError(false);
                }, 1000);
                return
            }
            setVacancy(vacancy_response)
        }
        catch {
            setGetError(true)
            setTimeout(() => {
                setGetError(false);
            }, 1000);
        }
    }

    return (
        <div className="container-xl py-4">
            <div className="d-flex justify-content-between align-items-center mb-4">
                <h1>Управление вакансиями</h1>
                {createError &&
                    <div className='alert alert-important alert-danger alert-dismissible' >
                        <p className='text-center'>{`Вакансия ${vacancyId} уже имеется в БД`}</p>
                    </div>}
                {getError &&
                    <div className='alert alert-important alert-danger alert-dismissible' >
                        <p className='text-center'>{`Вакансия ${vacancyId} не найдена в БД`}</p>
                    </div>}
                <div className="card">
                    <div className="d-flex gap-2 card-body">
                        <label className="form-label">HH.ru ID</label>
                        <input
                            className="form-control"
                            name="vacancy_id"
                            value={vacancyId}
                            onChange={(e) => setVacancyId(e.target.value)}
                            required
                        />
                        <div className="d-flex justify-content-end align-items-center gap-2">
                            <button onClick={createClick} className="btn btn-primary">
                                Спарсить с HH.ru
                            </button>
                            <button onClick={getClick} className="btn btn-primary">
                                Получить из БД
                            </button>
                        </div>
                    </div>
                </div>
                <button onClick={logout} className="btn btn-red">
                    Выйти
                </button>
            </div>
            {vacancy === undefined || vacancy === null ?
                <div className="card">
                    <div className="card-body">
                        <h2 className='text-center'>Введите ID вакансии для просмотра</h2>
                    </div>
                </div>
                : <VacancyView vacancy={vacancy} />}
        </div>
    );
}