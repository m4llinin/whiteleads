// src/components/Vacancy/VacancyForm.jsx
import { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { createVacancy, updateVacancy, getVacancy } from '../../api/vacancy';

export default function VacancyForm() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        hh_id: '',
        title: '',
        description: '',
        requirements: ''
    });
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        if (id) {
            const fetchData = async () => {
                setLoading(true);
                try {
                    const { data } = await getVacancy(id);
                    setFormData(data);
                } finally {
                    setLoading(false);
                }
            };
            fetchData();
        }
    }, [id]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (id) {
                await updateVacancy(id, formData);
            } else {
                await createVacancy(formData);
            }
            navigate('/');
        } catch (error) {
            console.error('Ошибка сохранения:', error);
        }
    };

    const handleChange = (e) => {
        setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
    };

    return (
        <div className="card">
            <div className="card-body">
                {loading && <div className="spinner-border"></div>}
                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label className="form-label">HH.ru ID</label>
                        <input
                            className="form-control"
                            name="hh_id"
                            value={formData.hh_id}
                            onChange={handleChange}
                            required
                        />
                    </div>

                    <div className="mb-3">
                        <label className="form-label">Название</label>
                        <input
                            className="form-control"
                            name="title"
                            value={formData.title}
                            onChange={handleChange}
                            required
                        />
                    </div>

                    <div className="mb-3">
                        <label className="form-label">Описание</label>
                        <textarea
                            className="form-control"
                            name="description"
                            value={formData.description}
                            onChange={handleChange}
                            rows="4"
                        />
                    </div>

                    <div className="mb-3">
                        <label className="form-label">Требования</label>
                        <textarea
                            className="form-control"
                            name="requirements"
                            value={formData.requirements}
                            onChange={handleChange}
                            rows="4"
                        />
                    </div>

                    <div className="d-flex justify-content-end gap-2">
                        <button type="submit" className="btn btn-primary">
                            {id ? 'Обновить' : 'Создать'}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}