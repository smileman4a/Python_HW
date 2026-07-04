from pages.shop_page import MainPage, LoginPage, CartPage, OrderPage
from selenium import webdriver
import pytest


@pytest.fixture
def setup_page():
    driver = webdriver.Firefox()
    driver.maximize_window()
    url = "https://www.saucedemo.com/"
    yield driver, url


def test_shop(setup_page):
    driver, url = setup_page
    page = LoginPage(driver, url)

    # Открыть сайт магазина.
    page.openLoginPage()

    # Авторизоваться как пользователь standard_user.
    page.usernameInput("standard_user")
    page.pwdInput("secret_sauce")
    page.loginClick()

    # Добавить в корзину товары:
    # # Sauce Labs Backpack.
    # # Sauce Labs Bolt T-Shirt.
    # # Sauce Labs Onesie.
    page = MainPage(driver)
    page.addToCart(page.BACKPACK)
    page.addToCart(page.BOLT_T_SHIRT)
    page.addToCart(page.ONESIE)

    # Перейти в корзину.
    page.cartClick()

    page = CartPage(driver)
    # Нажать кнопку Checkout.
    page.checkoutClick()

    page = OrderPage(driver)
    # Заполнить форму своими данными:
    # # Имя.
    # # Фамилия.
    # # Почтовый индекс.
    page.fillingForm("Тестимя", "Тестфамилия", "123456")
    page.continueClick()

    # Прочитать со страницы итоговую стоимость (Total).
    total = page.checkTotal()

    # Закрыть браузер.
    driver.quit()

    # Проверьте, что итоговая сумма равна $58.29.
    assert total.endswith("$58.29"), "Итоговая сумма не равна $58.29."
