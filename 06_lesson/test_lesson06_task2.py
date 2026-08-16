from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()


# Cookies пользователей
    user1_cookie = {
            "name": "SESSION",
            "value": "YWMyMGJkY2UtOGRkNC00YmUyLTllODEtNTZjZWJkZjg3YTcz",
            "domain": "gitflic.ru"
        }

    user2_cookie = {
            "name": "SESSION",
            "value": "YjU4ZDE0NDItZTA5ZC00YTQzLWFmMzMtOGE2OTdlMjRhNzQy",
            "domain": "gitflic.ru"
        }

# 1. Открытие страницы
    driver.get("https://gitflic.ru/")

# 2. Установить cookie пользователя 1
    driver.add_cookie(user1_cookie)

# 3. Обновить страницу
    driver.refresh()

# 4. Перейдите на страницу пользователя 1
    driver.get("https://gitflic.ru/user/cry56")

# 5. Сохраните текущий URL
    url_user1 = driver.current_url

# 6. Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()

# 7. Установите cookie пользователя 2
    driver.add_cookie(user2_cookie)

# 8. Обновите страницу
    driver.refresh()

# 9. Перейдите на страницу пользователя 2
    driver.get("https://gitflic.ru/user/sergo2")

# 10. Сохраните текущий URL
    url_user2 = driver.current_url

# 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются
    assert url_user1 != url_user2, f"URLs are the same: {url_user1}"

    driver.quit()
