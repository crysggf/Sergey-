import os
import requests
from dotenv import load_dotenv
load_dotenv()


class ProjectPage:
    """PageObject для работы с API проектов Yougile."""

    BASE_URL = "https://ru.yougile.com/api-v2/projects"

    def __init__(self, token=None):
        self.token = token or os.getenv("YOUGILE_TOKEN")
        if not self.token:
            raise ValueError(
                "Токен не найден. Установите переменную окружения "
                "YOUGILE_TOKEN."
            )
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def create_project(self, payload):
        """POST: создать проект."""
        return requests.post(
            self.BASE_URL, json=payload, headers=self.headers
        )

    def update_project(self, project_id, payload):
        """PUT: обновить проект по ID."""
        return requests.put(
            f"{self.BASE_URL}/{project_id}",
            json=payload,
            headers=self.headers,
        )

    def get_project(self, project_id):
        """GET: получить проект по ID."""
        return requests.get(
            f"{self.BASE_URL}/{project_id}", headers=self.headers
        )
