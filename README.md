# Whiteleads

---

## 📋 Предварительные требования

1. **Git** - система контроля версий:
    - [Скачать Git](https://git-scm.com/downloads)
    - Установите и настройте согласно инструкциям для вашей ОС

2. **Docker** и **Docker Compose**:
    - [Установка Docker](https://docs.docker.com/get-docker/)
    - [Установка Docker Compose](https://docs.docker.com/compose/install/)

---

## 🛠 Настройка окружения

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/m4llinin/whiteleads.git
   cd whiteleads
   ```

2. Создайте файл окружения:
    - Скопируйте шаблон:
      ```bash
      cp backend/env/example.env backend/env/prod.env
      ```
    - Заполните `prod.env`:

      ```ini
      # Настройки PostgreSQL
      DB_HOST=
      DB_PORT=
      DB_USERNAME=
      DB_PASSWORD=
      DB_DATABASE=
 
      # Настройки безопасности
      SECRET_KEY=
      ALGORITHM=
      ACCESS_TOKEN_EXPIRE_MINUTES=
      REFRESH_TOKEN_EXPIRE_DAYS=
 
      # Настройки CORS
      CORS_ORIGINS=
      CORS_CREDENTIALS=
      CORS_METHODS=
      CORS_HEADERS=
 
      # Режим работы
      MODE=
      ```

---

## 🚀 Запуск проекта

1. Соберите и запустите контейнеры:
   ```bash
   docker-compose up --build -d
   ```

2. Проверьте работу:
    - Бэкенд: `http://localhost:8000/docs`
    - Фронтенд: `http://localhost`
