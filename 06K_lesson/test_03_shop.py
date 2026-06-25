from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_buy_stuff():
    # Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Авторизуйтесь как пользователь standard_user.
    user_field = wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    user_field.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавьте в корзину товары:
    # Sauce Labs Backpack.
    # Sauce Labs Bolt T-Shirt.
    # Sauce Labs Onesie.
    driver.find_element(
        By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']"
    ).click()
    driver.find_element(
        By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
    ).click()
    driver.find_element(
        By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-onesie']"
    ).click()

    # Перейдите в корзину.
    driver.find_element(
        By.CSS_SELECTOR, "[data-test='shopping-cart-link']"
    ).click()

    # Нажмите Checkout.
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='checkout']"))
    ).click()

    # Заполните форму своими данными:
    # имя
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='firstName']")
        )
    ).send_keys("Тестимя")
    # фамилия
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='lastName']")
        )
    ).send_keys("Тестфамилия")
    # почтовый индекс
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='postalCode']")
        )
    ).send_keys("123456")

    # Нажмите кнопку Continue.
    driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()

    # Прочитайте со страницы итоговую стоимость (Total).
    total_cost = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "[data-test='total-label']")
    )).text

    # Закройте браузер.
    driver.quit()

    # Проверьте, что итоговая сумма равна $58.29.
    assert total_cost.endswith("$58.29"), "Итоговая сумма не равна $58.29."
