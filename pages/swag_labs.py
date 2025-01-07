from selenium.common import NoSuchElementException

from components.components import WebElement
from pages.base_page import BasePage


class SwagLabs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, 'div.login_logo')
        self.username_field = WebElement(driver, 'input#user-name')
        self.password_field = WebElement(driver, 'input#password')
