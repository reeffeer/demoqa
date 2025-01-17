import time

from conftest import browser
from pages.links import Links


def test_simple_link(browser):
    links = Links(browser)
    links.visit()

    assert links.home_link.exist()
    assert links.home_link.get_text() == 'Home'
    assert links.home_link.get_dom_attribute('href') == 'https://demoqa.com'

    links.home_link.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
