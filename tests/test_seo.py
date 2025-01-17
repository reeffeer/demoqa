import time

import pytest

from conftest import browser
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserWindows
from pages.demoqa_page import DemoQa


def test_check_title_demo(browser):
    demoqa_page = DemoQa(browser)

    demoqa_page.visit()
    assert browser.title == 'DEMOQA'


@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserWindows])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'


@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserWindows])
def test_meta(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
