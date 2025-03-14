// src/components/Auth/LoginForm.jsx
import { useState } from 'react';
import { useAuth } from '../../context/AuthContext';
import { Link, useNavigate } from 'react-router-dom';

export default function LoginForm() {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const { login } = useAuth();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await login({ username, password });
            navigate("/")
        }
        catch {

        }
    };

    return (
        <div className="card">
            <div className="card-body">
                <h2 className="card-title mb-4">Вход в систему</h2>
                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label className="form-label">Логин</label>
                        <input
                            type="text"
                            className="form-control"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            required
                        />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">Пароль</label>
                        <input
                            type="password"
                            className="form-control"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>
                    <p>Нет аккаунта? <Link to="/register">Создать</Link></p>
                    <button type="submit" className="btn btn-primary w-100">
                        Войти
                    </button>
                </form>
            </div>
        </div>
    );
}