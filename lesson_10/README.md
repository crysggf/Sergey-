# Домашнее задание 10: Allure + Page Object

Проект содержит UI-автотесты для калькулятора и интернет-магазина
с использованием паттерна Page Object и Allure для отчётности.

## Требования

- Python 3.8+
- Firefox браузер
- geckodriver.exe (в папке проекта)
- Java 8+ (для Allure)
- Allure Commandline

## Установка

### Клонируйте репозиторий

git clone <url_репозитория>
cd lesson_10

### Установите зависимости
pip install -r requirements.txt


### Скачайте geckodriver.exe

Скачайте и поместите `geckodriver.exe` в папку `lesson_10`:

https://github.com/mozilla/geckodriver/releases

### Установите Allure (если не установлен)

- Скачайте: https://github.com/allure-framework/allure2/releases
- Распакуйте в `C:\allure`
- Добавьте `C:\allure\bin` в переменную окружения PATH

## Запуск тестов

### Обычный запуск
pytest tests/ -v

### Запуск с формированием результатов для Allure

pytest tests/ --alluredir=allure-results


## Просмотр отчёта Allure

### Запуск локального сервера.

allure serve allure-results

Откроется браузер с интерактивным отчётом.

## Проверка стиля кода

flake8 . --max-line-length=120 --exclude=__pycache__,allure-results,allure-report
