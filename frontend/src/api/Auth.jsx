import axios from 'axios';

const api = axios.create({
    baseURL: '/api/v1'
});

export const signup = async (userData) => {
    const response = await api.post('/auth/signup', userData);
    return response.data;
};

export const login = async (credentials) => {
    const response = await api.post('/auth/login', credentials);
    return response.data;
};

export const refreshToken = async () => {
    const response = await api.post('/auth/refresh', {
        access_token: localStorage.getItem('access_token'),
        refresh_token: localStorage.getItem('refresh_token')
    })
    return response.data;
};

export const logout = async () => {
    const response = await api.post("/auth/logout", {
        access_token: localStorage.getItem('access_token'),
        refresh_token: localStorage.getItem('refresh_token')
    })
    window.location.reload()
    return response.data;
}