import axios from 'axios';
import { refreshToken } from './Auth';
import { useNavigate } from 'react-router-dom';

const api = axios.create({
    baseURL: '/api/v1',
    headers: {
        "WWW-Authorization": `Bearer ${localStorage.getItem('access_token')}`
    }
});

api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        if (error.response && error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            try {
                const data = await refreshToken()
                localStorage.setItem('access_token', data.access_token);
                originalRequest.headers['WWW-Authorization'] = `Bearer ${data.access_token}`;
                return api(originalRequest);
            } catch (refreshError) {
                console.error('Ошибка обновления токена:', refreshError);
                const navigate = useNavigate()
                navigate("/login")
            }
        }
    }
);

export const createVacancy = async (vacancy_id) => {
    const response = await api.post('/vacancy/create', { "vacancy_id": vacancy_id });
    return response.data;
};
export const updateVacancy = async (vacancy_id) => {
    const response = await api.patch(`/vacancy/update`, { "vacancy_id": vacancy_id });
    return response.data;
}
export const getVacancy = async (vacancy_id) => {
    const response = await api.get(`/vacancy/get/${vacancy_id}`);
    return response.data;
}
export const deleteVacancy = async (vacancy_id) => {
    const response = await api.delete(`/vacancy/delete/${vacancy_id}`);
    return response.data;
}