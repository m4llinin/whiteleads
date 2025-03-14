// src/pages/Login.jsx
import { useNavigate } from 'react-router-dom';
import LoginForm from '../components/Auth/LoginForm';
import { useAuth } from '../context/AuthContext';

export default function Login() {
    const navigate = useNavigate();
    const { login } = useAuth();

    const handleLogin = async (credentials) => {
        try {
            await login(credentials);
            navigate('/');
        } catch (error) {
            console.error('Ошибка входа:', error);
        }
    };

    return (
        <div className="container-tight py-4">
            <LoginForm onLogin={handleLogin} />
        </div>
    );
}