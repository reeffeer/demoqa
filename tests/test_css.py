from conftest import browser
from pages.text_box_page import TextBox


def test_text_box_submit(browser):
    text_box = TextBox(browser)

    text_box.visit()

    assert text_box.submit_btn.check_scc('color', 'rgba(255, 255, 255, 1)')
    assert text_box.submit_btn.check_scc('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert text_box.submit_btn.check_scc('borderColor', 'rgb(0, 123, 255)')
