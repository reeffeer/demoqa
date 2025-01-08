from components.components import WebElement
from pages.base_page import BasePage


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section_1_content = WebElement(driver, '#section1Content > p')
        self.section_1_heading = WebElement(driver, '#section1Heading')
        self.section_2_first_content = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section_2_second_content = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section_3_content = WebElement(driver, '#section3Content > p')
