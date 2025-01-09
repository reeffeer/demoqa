import time

from conftest import browser
from pages.text_box_page import TextBox


def test_text_box(browser):
    name_input = 'test text'
    address_input = 'Alabama'
    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys(name_input)
    text_box.current_address.send_keys(address_input)
    text_box.submit_btn.click()
    assert text_box.name_result.get_text() == f'Name:{name_input}'
    assert text_box.current_address_result.get_text() == f'Current Address :{address_input}'
