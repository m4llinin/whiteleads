// src/pages/Register.jsx
import { useNavigate } from 'react-router-dom';
import RegisterForm from '../components/Auth/RegisterForm';
import { useAuth } from '../context/AuthContext';

export default function Register() {
    const navigate = useNavigate();
    const { register } = useAuth();

    const handleRegister = async (userData) => {
        try {
            await register(userData);
            navigate('/login');
        } catch (error) {
            console.error('Ошибка регистрации:', error);
        }
    };

    return (
        <div className="container-tight py-4">
            <RegisterForm onRegister={handleRegister} />
        </div>
    );
}