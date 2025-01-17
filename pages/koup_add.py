from components.components import WebElement
from pages.base_page import BasePage


class KoupAdd(BasePage):
    def __init__(self, driver):
        self.btn_add = None
        self.btns_delete = None
        self.base_url = 'http://the-internet.herokuapp.com/add_remove_elements'
        super().__init__(driver, self.base_url)