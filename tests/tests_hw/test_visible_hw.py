import time

from conftest import browser
from pages.accordion import Accordion


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert accordion_page.section_1_content.visible()
    accordion_page.section_1_heading.click()
    time.sleep(2)
    assert not accordion_page.section_1_content.visible()


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert not accordion_page.section_2_first_content.visible()
    assert not accordion_page.section_2_second_content.visible()
    assert not accordion_page.section_3_content.visible()
