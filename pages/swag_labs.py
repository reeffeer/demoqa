from selenium.common import NoSuchElementException

from pages.base_page import BasePage


class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element('div.login_logo')
            return True
        except NoSuchElementException:
            return False
