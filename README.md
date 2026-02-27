# Django Greeter (кейс-задача №3)

Простое веб-приложение на Django:
- страница с формой ввода имени и кнопкой Submit;
- модель БД `NameEntry` с единственным полем `name`;
- сохранение введённого имени в SQLite и персональное приветствие на главной;
- обработка ошибки пустого имени (валидация формы);
- базовая стилизация через CSS;
- CSRF-защита включена стандартным middleware + `{% csrf_token %}` в форме.

## Запуск

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Откройте: http://127.0.0.1:8000/

## Админка (опционально)

```bash
python manage.py createsuperuser
```

Админка: http://127.0.0.1:8000/admin/

## Структура
- `greeter/` — приложение (модель, форма, вью, шаблоны, статика)
- `greeting_site/` — проект (настройки/urls)
