import uuid
import pytest
from project_page import ProjectPage


@pytest.fixture
def page():
    return ProjectPage()


def test_create_project_positive(page):
    unique_title = f"Test Project {uuid.uuid4().hex[:8]}"
    response = page.create_project({"title": unique_title})

    assert response.status_code == 201, response.text
    data = response.json()
    assert "id" in data

    project_id = data["id"]
    get_response = page.get_project(project_id)
    assert get_response.status_code == 200, get_response.text
    assert get_response.json()["title"] == unique_title


def test_create_project_negative(page):
    response = page.create_project({"description": "no title"})

    assert response.status_code == 400, response.text


def test_update_project_positive(page):
    created = page.create_project({"title": "Old title"}).json()
    project_id = created["id"]

    new_title = f"Updated {uuid.uuid4().hex[:8]}"
    response = page.update_project(project_id, {"title": new_title})

    assert response.status_code == 200, response.text


def test_update_project_negative(page):
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = page.update_project(fake_id, {"title": "New"})

    assert response.status_code == 404, response.text


def test_get_project_positive(page):
    created = page.create_project({"title": "For GET"}).json()
    project_id = created["id"]

    response = page.get_project(project_id)

    assert response.status_code == 200, response.text
    assert response.json()["id"] == project_id


def test_get_project_negative(page):
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = page.get_project(fake_id)

    assert response.status_code == 404, response.text
