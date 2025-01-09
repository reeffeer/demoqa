import time

from conftest import browser
from pages.text_box_page import TextBox


def test_placeholder(browser):
    text_box = TextBox(browser)

    text_box.visit()
    assert text_box.full_name.get_dom_attribute('placeholder') == 'Full Name'
