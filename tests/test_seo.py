from conftest import browser
from pages.demoqa_page import DemoQa


def test_check_title_demo(browser):
    demoqa_page = DemoQa(browser)

    demoqa_page.visit()
    assert browser.title == 'DEMOQA'
