# Как внести вклад в стайлгайд

## Предложение изменения

1. Создайте ветку от `main`: `git checkout -b docs/<тема>`.
2. Опишите проблему и номер правила.
3. Внесите правки и обновите связанные примеры.
4. Выполните проверки: `npm run lint:md`, `python scripts/check_examples.py`, `mkdocs build --strict`.
5. Создайте Pull Request в `main`.

## Коммиты

Формат: `<type>(<scope>): <описание>`.
Типы: `docs`, `fix`, `ci`, `test`, `chore`.

Пример: `docs(accessibility): add text accessibility rules`.

## Ревью

Автор сообщает цель и результаты проверок. Ревьюер проверяет текст и страницы.
Замечания адресуются отдельным коммитом. Merge — после одобрения и зелёного CI.

## Локальная сборка

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
npm ci
npm run lint:md
python scripts/check_examples.py
mkdocs build --strict
mkdocs serve
```

## Добавление нового раздела

1. Создайте `.md` в `docs/guide/`.
2. Задайте уникальные идентификаторы правил.
3. Добавьте страницу в `nav` в `mkdocs.yml`.
4. Обновите ссылки и историю версий.
5. Выполните проверки и откройте PR.