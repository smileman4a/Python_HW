from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    # Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")

    # Установите cookie пользователя 1.
    driver.add_cookie(
        {
            "name": "SESSION",
            "value": "NDVhM2RlNTctOGY5YS00MGQzLWJlNzgtNDQ5YjZlNzhhNTJl",
            "domain": "gitflic.ru",
        }
    )
    driver.add_cookie(
        {"name": "cookiesAccepted", "value": "true", "domain": "gitflic.ru"}
    )

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 1.
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/header/div/div/div[2]/a/p")
        )
    )
    driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/a/p").click()

    # Сохраните текущий URL.
    user1_url = driver.current_url

    # Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
    driver.get("https://gitflic.ru/")

    # Установите cookie пользователя 2.
    driver.add_cookie(
        {
            "name": "SESSION",
            "value": "ZmI2OTI2ODgtZGRjMi00YmMyLTg2ZTEtMWE1YTNjNzI4NWU5",
            "domain": "gitflic.ru",
        }
    )
    driver.add_cookie(
        {"name": "cookiesAccepted", "value": "true", "domain": "gitflic.ru"}
    )

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 2.
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/header/div/div/div[2]/a/p")
        )
    )
    driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/a/p").click()

    # Сохраните текущий URL.
    user2_url = driver.current_url

    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert user1_url != user2_url, "Что-то пошло не так!"

    driver.quit()
