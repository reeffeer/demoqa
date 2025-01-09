import time

from conftest import browser
from pages.text_box_page import TextBox


def test_clear(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys('test')
    time.sleep(2)
    text_box.full_name.clear()
    time.sleep(2)
    assert text_box.full_name.get_text() == ''
