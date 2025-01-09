from components.components import WebElement
from pages.base_page import BasePage


class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '//*[@id="userName"]', locator_type='xpath')
        self.current_address = WebElement(driver, '#currentAddress')
        self.submit_btn = WebElement(driver, '#submit')
        self.name_result = WebElement(driver, '//*[@id="name"]', 'xpath')
        self.current_address_result = WebElement(driver, '//*[@id="output"]/div/p[@id="currentAddress"]', 'xpath')
