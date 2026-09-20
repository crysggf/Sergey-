from sqlalchemy import text


def test_create_subject(engine, subject_factory):
    created = subject_factory()

    with engine.connect() as conn:
        result = conn.execute(
            text(
                "SELECT subject_title FROM subject "
                "WHERE subject_id = :id"
            ),
            {"id": created["id"]},
        )
        row = result.fetchone()

    assert row is not None, "Созданный предмет не найден в БД"
    assert row[0] == created["title"]


def test_update_subject(engine, subject_factory):
    created = subject_factory()

    new_title = f"Updated {created['title']}"
    with engine.begin() as conn:
        conn.execute(
            text(
                "UPDATE subject SET subject_title = :title "
                "WHERE subject_id = :id"
            ),
            {"title": new_title, "id": created["id"]},
        )

    with engine.connect() as conn:
        result = conn.execute(
            text(
                "SELECT subject_title FROM subject "
                "WHERE subject_id = :id"
            ),
            {"id": created["id"]},
        )
        row = result.fetchone()

    assert row is not None
    assert row[0] == new_title


def test_delete_subject(engine, subject_factory):
    created = subject_factory()

    with engine.begin() as conn:
        conn.execute(
            text("DELETE FROM subject WHERE subject_id = :id"),
            {"id": created["id"]},
        )

    with engine.connect() as conn:
        result = conn.execute(
            text(
                "SELECT COUNT(*) FROM subject "
                "WHERE subject_id = :id"
            ),
            {"id": created["id"]},
        )
        count = result.scalar()

    assert count == 0, "Предмет не был удалён"
