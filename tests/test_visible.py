import time

from conftest import browser
from pages.elements import ElementsPage


def test_visible_sidebar(browser):
    el_page = ElementsPage(browser)

    el_page.visit()
    assert el_page.btn_sidebar_first_textbox.visible()


def test_not_visible_sidebar(browser):
    el_page = ElementsPage(browser)

    el_page.visit()
    assert el_page.btn_sidebar_first_checkbox.visible()
    el_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not el_page.btn_sidebar_first_checkbox.visible()
