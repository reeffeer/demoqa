import time

from conftest import browser
from pages.browser_tab import BrowserWindows


def test_tab(browser):
    tab = BrowserWindows(browser)
    tab.visit()

    assert len(browser.window_handles) == 1
    tab.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)

