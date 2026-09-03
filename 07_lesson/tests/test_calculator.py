from pages.calculator_page import CalculatorPage


def test_calculator_with_delay(driver):
    calculator = CalculatorPage(driver)

    calculator.open()
    calculator.set_delay(5)
    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')

    result = calculator.get_result()

    assert result == "15", f"Expected '15', got '{result}'"
