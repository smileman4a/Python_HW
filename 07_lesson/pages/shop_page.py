from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    LOGIN_INPUT = (By.ID, "user-name")
    PWD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    def open_login_page(self):
        self.driver.get(self.url)

    def username_input(self, username):
        self.wait.until(
            EC.presence_of_element_located(self.LOGIN_INPUT)
        ).send_keys(username)

    def pwd_input(self, pwd):
        self.wait.until(
            EC.presence_of_element_located(self.PWD_INPUT)
        ).send_keys(pwd)

    def login_click(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()


class MainPage:
    BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    BOLT_T_SHIRT = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ONESIE = (By.ID, 'add-to-cart-sauce-labs-onesie')
    CART = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, good):
        self.wait.until(EC.element_to_be_clickable(good)).click()

    def cart_click(self):
        self.wait.until(EC.element_to_be_clickable(self.CART)).click()


class CartPage:
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)

    def checkout_click(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()


class OrderPage:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "[data-test='lastName']")
    ZIP_INPUT = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    TOTAL_COST = (By.CSS_SELECTOR, "[data-test='total-label']")

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)

    def filling_form(self, name, surname, zip_code):
        self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        ).send_keys(name)
        self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME_INPUT)
        ).send_keys(surname)
        self.wait.until(
            EC.presence_of_element_located(self.ZIP_INPUT)
        ).send_keys(zip_code)

    def continue_click(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def check_total(self):
        total_cost = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_COST)
        ).text
        return total_cost
