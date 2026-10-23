# Справочник операции GET /rooms/{id}/availability

**Аудитория:** разработчики интеграций.
**Версия API:** 1.0.0.

## Назначение

Получить список свободных интервалов комнаты на дату.

## Метод и путь

`GET /rooms/{id}/availability`

## Авторизация

Bearer-токен.

## Параметры пути

| Параметр | Тип | Обязательный | Ограничения |
|----------|-----|--------------|-------------|
| `id` | integer | да | от 1 до 9999 |

## Параметры запроса

| Параметр | Тип | Обязательный | Ограничения |
|----------|-----|--------------|-------------|
| `date` | string (date) | да | формат `YYYY-MM-DD` |

## Успешный ответ 200 OK

```json
{
  "room_id": 101,
  "date": "2026-11-20",
  "slots": [
    { "start": "10:00Z", "end": "11:00Z" },
    { "start": "14:00Z", "end": "15:30Z" }
  ]
}
```

## Ошибки

Формат ошибок соответствует RFC 9457 (Content-Type: application/problem+json).

```json
{
  "type": "https://api.example.test/errors/room-not-found",
  "title": "Room not found",
  "status": 404,
  "detail": "Room with id 102 does not exist",
  "instance": "/rooms/102/availability"
}
```