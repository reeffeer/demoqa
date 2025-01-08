from conftest import browser
from pages.demoqa_page import DemoQa
from pages.elements import ElementsPage


def test_check_text_footer(browser):
    demoqa_page = DemoQa(browser)
    el_page = ElementsPage(browser)

    demoqa_page.visit()
    demoqa_page.btn_elements.click()
    
    el_page.refresh()
    browser.refresh()
    browser.back()
    assert demoqa_page.get_url() == browser.current_url
    browser.forward()
    assert el_page.equal_url()
