# Как забронировать переговорную через API

**Аудитория:** разработчики интеграций, знакомые с HTTP и JSON.
**Версия API:** 1.0.0.

## Условия

- получен тестовый токен;
- известен идентификатор комнаты;
- комната доступна в выбранное время.

## Шаги

1. Проверьте доступность комнаты.

```http
GET /rooms/101/availability?date=2026-11-20 HTTP/1.1
Host: api.example.test
Authorization: Bearer test-token
```

Ожидаемый результат: сервер вернул список свободных слотов.

2. Создайте бронирование.

```http
POST /bookings HTTP/1.1
Host: api.example.test
Authorization: Bearer test-token
Content-Type: application/json
```

```json
{
  "room_id": 101,
  "start": "2026-11-20T10:00:00Z",
  "end": "2026-11-20T11:00:00Z",
  "title": "Синк команды"
}
```

**Результат:** сервер вернул `201 Created` и объект бронирования с полем `id`.

```json
{
  "id": 5541,
  "room_id": 101,
  "status": "confirmed"
}
```

## Ошибки

Формат ошибок соответствует RFC 9457 (Content-Type: application/problem+json).

```json
{
  "type": "https://api.example.test/errors/invalid-token",
  "title": "Unauthorized",
  "status": 401,
  "detail": "Token is missing or expired"
}
```