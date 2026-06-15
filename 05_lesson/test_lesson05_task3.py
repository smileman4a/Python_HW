from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_multiple_elements():
    driver = webdriver.Chrome()

    # # Откройте страницу https://httpbin.org/links/10.
    driver.get("https://httpbin.org/links/10")
    sleep(1)

    # # Найдите все ссылки на странице (тег <a>).
    links = driver.find_elements(By.TAG_NAME, "a")

    # # Проверьте, что количество ссылок равно 9.
    assert len(links) == 9

    # # Проверьте, что все ссылки отображаются на странице.
    for link in links:
        assert link.is_displayed()

    # # Проверьте, что текст первой ссылки содержит "1".
    assert "1" in links[0].text

    driver.quit()
