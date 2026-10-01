"""Тесты для калькулятора."""

import allure
from pages.calculator_page import CalculatorPage


@allure.title("Проверка работы калькулятора с задержкой")
@allure.description(
    "Тест проверяет, что калькулятор корректно выполняет "
    "сложение 7 + 8 = 15 с установленной задержкой"
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_with_delay(driver):
    """Тест проверки калькулятора."""
    calculator = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator.open()

    with allure.step("Установить задержку 5 секунд"):
        calculator.set_delay(5)

    with allure.step("Нажать кнопки 7 + 8 ="):
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')
        calculator.click_button('=')

    with allure.step("Дождаться появления результата 15"):
        calculator.wait_for_result("15")

    with allure.step("Получить результат"):
        result = calculator.get_result()

    with allure.step("Проверить, что результат равен 15"):
        assert result == "15", f"Expected '15', got '{result}'"
