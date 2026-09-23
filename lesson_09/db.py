import os

from sqlalchemy import create_engine

DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"


def get_engine():
    password = os.getenv("PG_PASSWORD")
    if not password:
        raise ValueError(
            "Не найден пароль. Установите переменную окружения "
            "PG_PASSWORD."
        )
    url = (
        f"postgresql://{DB_USER}:{password}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    return create_engine(url)
