from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start"
    driver.find_element(By.XPATH, "//button[text()='Start']").click()

    # 3. Дождитесь появления текста "Hello World!"
    wait.until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="finish"]/h4'), "Hello World!"
        )
    )
    message_element = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')

    # 4. Сделайте скриншот страницы
    driver.get_screenshot_as_file("screenshot.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert message_element.text == "Hello World!", (
        "Сообщение 'Hello World!' не появилось"
    )
    driver.quit()
