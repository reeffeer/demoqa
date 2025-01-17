import time

from conftest import browser
from pages.web_tables import WebTables


def test_tab(browser):
    tables = WebTables(browser)
    tables.visit()

    headers = tables.header.find_elements()

    for head in headers:
        head.click()
        time.sleep(2)
        assert '-sort-' in head.get_dom_attribute('class'), "Doesn't sort"
