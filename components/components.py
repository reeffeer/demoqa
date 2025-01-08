from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def get_text(self):
        element = self.find_element()
        return str(element.text)

    def find_element(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, self.locator)
        except NoSuchElementException as e:
            print(f"Элемент не найден: {e}")

    def find_elements(self):
        try:
            return self.driver.find_elements(By.CSS_SELECTOR, self.locator)
        except NoSuchElementException as e:
            print(f"Элементы не найдены: {e}")

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    def exist(self):
        try:
            self.find_element()
            return True
        except NoSuchElementException:
            return False

    def click(self):
        try:
            element = self.find_element()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
            # self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print(f"Ошибка при клике на элемент: {e}")

    def force_click(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def visible(self):
        return self.find_element().is_displayed()

    def send_keys(self, text: str):
        self.find_element().send_keys(text)
