import time

from conftest import browser
from pages.demoqa_page import DemoQa


def test_size(browser):
    demoqa_page = DemoQa(browser)

    demoqa_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)
