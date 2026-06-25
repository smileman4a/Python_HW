from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    # в Google Chrome.
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    # В поле ввода по локатору #delay введите значение 45.
    delay_field = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    delay_field.clear()
    delay_field.send_keys(45)

    # Нажмите на кнопки: '7', '+', '8', '='
    keys_container = driver.find_element(By.CSS_SELECTOR, "div.keys")
    for ky in "7+8=":
        keys_container.find_element(
            By.XPATH, f".//span[text()='{ky}']"
        ).click()

    # Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    result_locator = (By.CSS_SELECTOR, "#calculator div.screen")
    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element(result_locator, "15")
    )
    result_text = driver.find_element(*result_locator).text
    assert result_text == "15", \
        f"Ожидался результат 15, но получен {result_text}"

    driver.quit()
