from components.components import WebElement
from pages.base_page import BasePage


class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, '//*[@class="rt-noData"]', 'xpath')
        self.btn_delete_rows = WebElement(driver, "//*[@id[contains(., 'delete-record-')]]", 'xpath')
        self.delete = WebElement(driver, "//*[@id='delete-record-4']", 'xpath')
        self.edit = WebElement(driver, "")
        self.btn_add = WebElement(driver, '#addNewRecordButton')

        self.reg_form = WebElement(driver, '#registration-form-modal')
        self.btn_submit = WebElement(driver, '#submit')
        self.user_form = WebElement(driver, '//*[@id="userForm"]', 'xpath')

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')

        self.row = WebElement(driver, "//div[@class='rt-tr-group' and @role='rowgroup']", 'xpath')
        self.rows_per_page = WebElement(driver, 'div.-center > span.select-wrap.-pageSizeOptions > select')
        self.next = WebElement(driver, "div.-next > button")
        self.previous = WebElement(driver, "div.-previous> button")
        self.total_pages = WebElement(driver, "div.-center > span.-pageInfo > span")
        self.page_number = WebElement(driver, "span.-pageInfo > div > input[type=number]")

        self.header = WebElement(driver, "div.rt-thead.-header > div > div")
