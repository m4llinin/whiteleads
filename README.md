# Whiteleads
Проект для парсинга вакансий с hh.ru и сохранения их локально в БД
---

# Технологии  
FastAPI, PostgreSQL, AsyncPG, SQLAlchemy 2.0, Alembic, Uvicorn, MyPy, Pydantic, JavaScript, React, Vite, Nginx, Docker, Docker Compose

# Функции
- Парсинг вакансии с hh.ru
- Сохранение вакансии в БД
- Изменение вакансии в БД

## Запуск

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/m4llinin/whiteleads.git
   cd whiteleads
   ```

2. Создайте файл окружения backend/env/prod.env:
   Скопируйте шаблон:
   ```bash
   cp backend/env/example.env backend/env/prod.env
   ```
      
3. Соберите и запустите контейнеры:
   ```bash
   docker compose up --build -d
   ```
