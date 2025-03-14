import { useState } from 'react';
import { useAuth } from '../../context/AuthContext';
import { Link, useNavigate } from 'react-router-dom';

export default function RegisterForm() {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const { signup } = useAuth();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await signup({ username, password });
            navigate("/login")
        }
        catch {
            console.error("SignUpError")
        }
    };

    return (
        <div className="card">
            <div className="card-body">
                <h2 className="card-title mb-4">Регистрация</h2>
                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label className="form-label">Имя пользователя</label>
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
                    <p>Есть аккаунт? <Link to="/login">Войти</Link></p>
                    <button type="submit" className="btn btn-primary w-100">
                        Зарегистрироваться
                    </button>
                </form>
            </div>
        </div>
    );
}