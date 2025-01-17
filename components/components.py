from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class WebElement:
    def __init__(self, driver, locator='', locator_type='css'):
        self.locator_type = locator_type
        self.driver = driver
        self.locator = locator

    def get_text(self):
        element = self.find_element()
        return str(element.text)

    def find_element(self):
        try:
            return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((self.get_by_type(), self.locator)))
        except NoSuchElementException as e:
            print(f"Элемент не найден: {e}")
            return None

    def find_elements(self):
        try:
            return self.driver.find_elements(self.get_by_type(), self.locator)
        except NoSuchElementException as e:
            print(f"Элементы не найдены: {e}")

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    def exist(self):
        if self.find_element():
            return True

        return False

    def not_exist(self):
        element = self.find_element()
        return element is None

    def click(self):
        try:
            element = self.find_element()
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.scroll_to_element()
            element.click()
            # self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print(f"Ошибка при клике на элемент: {e}")

    def force_click(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def scroll_to_element(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", self.find_element())

    def visible(self):
        return self.find_element().is_displayed()

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    @staticmethod
    def fill_form(elements, params):
        if len(elements) != len(params):
            raise ValueError("Number of elements and parameters should be the same")

        for el, par in zip(elements, params):
            el.send_keys(par)

    def clear(self):
        self.send_keys(Keys.CONTROL + 'a')
        self.send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'xpath':
            return By.XPATH
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('Locator type ' + self.locator_type + ' is incorrect')
            return False

    def check_scc(self, style, value=''):
        return self.find_element().value_of_css_property(style) == value

    def select_by_index(self, index: int):
        return Select(self.find_element()).select_by_index(index)

