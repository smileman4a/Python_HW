from pages.shop_page import MainPage, LoginPage, CartPage, OrderPage
from selenium import webdriver
import pytest


@pytest.fixture
def setup_page():
    driver = webdriver.Firefox()
    driver.maximize_window()
    url = "https://www.saucedemo.com/"
    yield driver, url
    driver.quit()


def test_shop(setup_page):
    driver, url = setup_page
    page = LoginPage(driver, url)

    # Открыть сайт магазина.
    page.open_login_page()

    # Авторизоваться как пользователь standard_user.
    page.username_input("standard_user")
    page.pwd_input("secret_sauce")
    page.login_click()

    # Добавить в корзину товары:
    # # Sauce Labs Backpack.
    # # Sauce Labs Bolt T-Shirt.
    # # Sauce Labs Onesie.
    page = MainPage(driver)
    page.add_to_cart(page.BACKPACK)
    page.add_to_cart(page.BOLT_T_SHIRT)
    page.add_to_cart(page.ONESIE)

    # Перейти в корзину.
    page.cart_click()

    page = CartPage(driver)
    # Нажать кнопку Checkout.
    page.checkout_click()

    page = OrderPage(driver)
    # Заполнить форму своими данными:
    # # Имя.
    # # Фамилия.
    # # Почтовый индекс.
    page.filling_form("Тестимя", "Тестфамилия", "123456")
    page.continue_click()

    # Прочитать со страницы итоговую стоимость (Total).
    total = page.check_total()

    # Проверьте, что итоговая сумма равна $58.29.
    assert total.endswith("$58.29"), "Итоговая сумма не равна $58.29."
