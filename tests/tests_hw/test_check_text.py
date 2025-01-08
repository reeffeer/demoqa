from conftest import browser
from pages.demoqa_page import DemoQa
from pages.elements import ElementsPage


def test_check_text_footer(browser):
    demoqa_page = DemoQa(browser)

    demoqa_page.visit()
    assert demoqa_page.equal_url()
    demoqa_page.footer.find_element()
    footer_text = demoqa_page.footer.get_text()
    expected_footer_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    assert footer_text == expected_footer_text, f"Expected: '{expected_footer_text}', but got: '{footer_text}'"


def test_check_text_on_center_elements_page(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.equal_url()
    central_text = elements_page.central_text.get_text()
    expected_text = 'Please select an item from left to start practice.'
    assert central_text == expected_text, f"Expected: '{expected_text}', but got: '{central_text}'"
