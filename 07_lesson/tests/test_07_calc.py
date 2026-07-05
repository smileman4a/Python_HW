from pages.calc_page import CalcPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def setup_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = "https://bonigarcia.dev" \
        "/selenium-webdriver-java/slow-calculator.html"
    yield driver, url
    driver.quit()


def test_calc(setup_page):
    driver, url = setup_page
    page = CalcPage(driver, url)

    # Открыть страницу калькулятора.
    page.open_calc_page()

    # Ввести значение 45 в поле задержки (локатор #delay).
    page.delay_input(45)

    # Нажать кнопки: 7, +, 8, =.
    for button in '7+8=':
        page.calc_input(button)

    # Проверить (assert), что в окне отобразится результат 15 через 45 секунд.
    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element(page.RESULT_FIELD, "15")
    )
    result_text = driver.find_element(*page.RESULT_FIELD).text
    assert result_text == "15", \
        f"Ожидался результат 15, но получен {result_text}"
