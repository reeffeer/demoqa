from conftest import browser
import time
from pages.swag_labs import SwagLabs


def test_check_icon(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    time.sleep(5)
    swag_labs_page.icon.exist()
    time.sleep(3)


def test_check_name_field(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    time.sleep(5)
    swag_labs_page.username_field.find_element()


def test_check_password_field(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    time.sleep(5)
    swag_labs_page.password_field.find_element()
