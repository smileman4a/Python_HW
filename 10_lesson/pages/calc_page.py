from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    DELAY_INPUT_FIELD = (By.ID, "delay")  # поле ввода задержки

    BUTTONS = {}  # кнопки на калькуляторе
    for symb in "789+456-123÷0.=xC":
        BUTTONS[symb] = (By.XPATH, f".//span[text()='{symb}']")

    # поле результата
    RESULT_FIELD = (By.CSS_SELECTOR, "#calculator div.screen")

    def __init__(self, driver, url):
        """
        Конструктор класса CalcPage.

        :param driver: WebDriver — объект драйвера Selenium.
        :param url: BaseURL - url страницы калькулятора
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы калькулятора")
    def open_calc_page(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(self.url)

    @allure.step("Установка задержки {delay} секунд")
    def delay_input(self, delay):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param delay: int — время задержки в секундах.
        """
        delay_field = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT_FIELD)
            )
        delay_field.clear()
        delay_field.send_keys(delay)

    @allure.step("Нажатие кнопки '{button}'")
    def calc_input(self, button):
        """
        Нажимает на кнопку калькулятора.

        :param button: str — текст на кнопке, которую нужно нажать.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTONS[button])
            ).click()
