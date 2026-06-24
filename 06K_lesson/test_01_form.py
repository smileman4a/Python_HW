from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color

driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)


def test_form():
    # Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    # в Edge или Safari.
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполните форму значениями:
    values = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "job-position": "QA",
        "company": "SkyPro",
    }
    forms = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "form-control"))
    )
    for form in forms:
        name_form = form.get_attribute("name")
        form.send_keys(values[name_form])

    # Нажмите кнопку Submit.
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    button.click()

    # Проверьте (assert), что поле Zip code подсвечено красным.
    # Проверьте (assert), что остальные поля подсвечены зеленым.
    for id in values.keys():
        form = driver.find_element(By.ID, id)
        back_color = form.value_of_css_property("background-color")
        hex_color = Color.from_string(back_color).hex
        if id == "zip-code":
            assert hex_color == "#f8d7da", "Поле Zip code не подсвечено красным"
        else:
            assert hex_color == "#d1e7dd", f"Поле {id} не подсвечено зеленым"

    driver.quit()
