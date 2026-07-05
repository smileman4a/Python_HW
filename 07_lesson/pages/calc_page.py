from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    DELAY_INPUT_FIELD = (By.ID, "delay")  # поле ввода задержки

    BUTTONS = {}  # кнопки на калькуляторе
    for symb in "789+456-123÷0.=xC":
        BUTTONS[symb] = (By.XPATH, f".//span[text()='{symb}']")

    # поле результата
    RESULT_FIELD = (By.CSS_SELECTOR, "#calculator div.screen")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    def open_calc_page(self):
        self.driver.get(self.url)

    def delay_input(self, delay):
        delay_field = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT_FIELD)
            )
        delay_field.clear()
        delay_field.send_keys(delay)

    def calc_input(self, button):
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTONS[button])
            ).click()
