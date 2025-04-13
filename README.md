# README.md

# Reservation Service

Сервис для бронирования столиков в ресторане с валидацией пересечений по времени.

##  Стек технологий
- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0 + asyncpg
- Alembic (миграции)
- Docker / docker-compose

##  Запуск в Docker

```bash
docker-compose up --build
```

##  API

После запуска API доступен на:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

##  Примеры запросов

### Создание столика
POST `/tables/`
```json
{
  "name": "Table 1",
  "seats": 4,
  "location": "Window"
}
```

### Создание брони (при отсутствии пересечений)
POST `/reservations/`
```json
{
  "customer_name": "Alice",
  "table_id": 1,
  "reservation_time": "2025-04-11T15:00:00",
  "duration_minutes": 60
}
```

## Валидация пересечений
Нельзя создать бронь, если:
- указанный `table_id` уже занят в пересекающийся временной интервал.
- в таком случае возвращается ошибка 400 с сообщением:
```json
{
  "detail": "This table is already reserved at that time"
}
```

## Переменные окружения
Файл `.env`:
```
DATABASE_URL=postgresql+asyncpg://postgres:postgre@db:5432/reservation_db
```

## Структура проекта
`reservation_service/` — разделён на модули: `routers`, `schemas`, `services`, `models`, `core`, `db`.

## Миграции
```bash
alembic revision --autogenerate -m "msg"
alembic upgrade head
```
(автоматически применяются в контейнере при запуске)

## 🧪 Тесты
Папка `tests/` предназначена для тестов на `pytest` (опционально).

