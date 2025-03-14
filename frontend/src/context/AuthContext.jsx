import { createContext, useContext, useState } from 'react';
import { login, signup, logout } from '../../src/api/Auth';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {

    const handleAuth = async (authFn, credentials) => {
        try {
            const tokens = await authFn(credentials);
            localStorage.setItem('access_token', tokens.access_token);
            localStorage.setItem('refresh_token', tokens.refresh_token);
            localStorage.setItem("user", credentials.username)
        } catch (error) {
            console.error('Auth error:', error);
        }
    };

    const user = () => localStorage.getItem("user")
    const authLogin = (credentials) => handleAuth(login, credentials);
    const authSignUp = (credentials) => handleAuth(signup, credentials);
    const authLogOut = async () => {
        try {
            await logout()
            localStorage.removeItem("user");
            localStorage.removeItem("access_token");
            localStorage.removeItem("refresh_token");
        }
        catch {

        }
    }

    return (
        <AuthContext.Provider value={{ user, login: authLogin, signup: authSignUp, logout: authLogOut }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);