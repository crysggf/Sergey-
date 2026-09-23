# Sergey- Автоматизация Python

Учебный проект по автоматизациии тестирования на Python.

## lesson_09 - тесты базы данных PostgreSQL

Домашнее задание №9: тесты для работы с БД PostgreSQL через библиотеку SQLAlchemy.

Тестируется таблица 'subject' в базе данных 'postgres':
- "Create" Добавление нового предмета;
- "update" изменение названия предмета;
- "delete" удаление предмета.

### Требования
- Python 3.10+
- PostgreSQL (запущенный локально)
- База данных 'postgres' с таблицами 'student', 'subject', 'teacher'
- установленные библиотеки: pip install pytest sqlalchemy psycopg2-binary 