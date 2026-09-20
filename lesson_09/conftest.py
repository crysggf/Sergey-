import random

import pytest
from sqlalchemy import text

from db import get_engine

@pytest.fixture(scope="session")
def engine():
    return get_engine()

@pytest.fixture
def subject_factory(engine):
    created_ids = []

    def _create(subject_id=None, title=None):
        if subject_id is None:
            subject_id = random.randint(900000, 999999)
        if title is None:
            title = f"Test Subject {subject_id}"
        with engine.begin() as conn:
            conn.execute(
                text(
                    "INSERT INTO subject (subject_id, subject_title) "
                    "VALUES (:id, :title)"
                ),
                {"id": subject_id, "title": title},
            )
        created_ids.append(subject_id)
        return {"id": subject_id, "title": title}

    yield _create

    with engine.begin() as conn:
        for sid in created_ids:
            conn.execute(
                text("DELETE FROM subject WHERE subject_id = :id"),
                {"id": sid},
            )
