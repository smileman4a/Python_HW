from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_form_submission():
    driver = webdriver.Chrome()

    # # Откройте страницу https://httpbin.org/forms/post.
    driver.get("https://httpbin.org/forms/post")
    sleep(1)
    home_url = driver.current_url

    # # Найдите поле ввода с названием custname.
    custname = driver.find_element(By.NAME, "custname")

    # # Введите в него ваше имя.
    custname.send_keys("Константин")

    # # Найдите кнопку Submit и нажмите на нее.
    button = driver.find_element(By.XPATH, "/html/body/form/p[6]/button")
    button.click()

    # # Проверьте, что после нажатия URL изменился.
    sleep(1)
    assert driver.current_url != home_url

    driver.quit()
