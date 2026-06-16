from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_navigation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # # Откройте страницу https://httpbin.org/.
    driver.get("https://httpbin.org/")
    sleep(1)

    # # Найдите и кликните на ссылку HTML Form.
    driver.find_element(By.LINK_TEXT, "HTML form").click()
    sleep(1)

    # # Проверьте, что URL изменился на /forms/post.
    assert driver.current_url.endswith("/forms/post")

    # # Вернитесь назад на главную страницу.
    driver.back()
    sleep(1)

    # # Проверьте, что вернулись на исходный URL.
    assert driver.current_url == "https://httpbin.org/"

    driver.quit()
