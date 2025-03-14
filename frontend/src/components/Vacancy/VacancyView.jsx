import { useNavigate } from 'react-router-dom';
import { updateVacancy, deleteVacancy } from '../../../src/api/Vacancy';
import DOMPurify from 'dompurify';

function VacancyView({ vacancy }) {
    const navigate = useNavigate()
    const reformatDate = (data) => {
        const date = new Date(data);
        const formattedDate = date.toLocaleString('ru-RU', {
            day: 'numeric',
            month: 'long',
            year: 'numeric',
            hour: 'numeric',
            minute: 'numeric',
            second: 'numeric',
        });
        return formattedDate;
    }

    const handleUpdateCLick = (e) => {
        updateVacancy({ "vacancy_id": vacancy.vacancy_id })
    }

    const handleDeleteCLick = (e) => {
        deleteVacancy(vacancy.vacancy_id)
        window.location.reload();
    }


    return (
        <div className='button-conteiner'>
            <div className="card">
                <div className="card-body">
                    <div className='card-header mb-3'>
                        <h2 className="card-title">Вакансия</h2>
                    </div>
                    <div className="mb-4">
                        <h3>HH.ru ID</h3>
                        <p className="text-muted">{vacancy["vacancy_id"]}</p>
                    </div>

                    <div className="mb-4">
                        <h3>Название вакансии</h3>
                        <p className="text-muted">{vacancy["vacancy_name"]}</p>
                    </div>

                    <div className="mb-4">
                        <h3>Описание</h3>
                        <div className="text-muted" dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(vacancy["description"]) }} />
                    </div>

                    <div className="mb-4">
                        <h3>Статус вакансии</h3>
                        <p className="text-muted">{vacancy["archived"] ? "Архивирована" : "Актуальна"}</p>
                    </div>
                    <div className="mb-4">
                        <h3>Создана</h3>
                        <p className="text-muted">{reformatDate(vacancy["vacancy_created_at"])}</p>
                    </div>
                </div>
            </div>
            <div className="card">
                <div className="card-body">
                    <div className='card-header mb-3'>
                        <h3 className="card-title">Работодатель</h3>
                    </div>
                    <div className="mb-4 d-flex gap-3">
                        <img
                            src={vacancy["company_logo"]}
                            alt="Логотип"
                            loading="lazy"
                            onError={(e) => {
                                e.target.style.display = 'none';
                            }}
                            width="100px"
                            className='border border-primary rounded-2'
                        />
                        <div className="mb-4">
                            <h3>Название компании</h3>
                            <p className="text-muted">{vacancy["company_name"]}</p>
                        </div>
                        <div className="mb-4">
                            <h3>Адрес офиса</h3>
                            <p className="text-muted">{vacancy["company_address"]}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div className='d-flex gap-3'>
                <a
                    href={`https://hh.ru/vacancy/${vacancy["vacancy_id"]}`}
                    className="btn btn-outline-primary"
                    target="_blank"
                    rel="noreferrer"
                >
                    На HH.ru
                </a>
                <button onClick={handleUpdateCLick} className="btn btn-primary">
                    Обновить
                </button>
                <button onClick={handleDeleteCLick} className="btn btn-primary">
                    Удалить
                </button>
            </div>
        </div>
    );
}

export default VacancyView;