import time

from selenium.webdriver import Keys

from conftest import browser
from pages.form_page import FormPage


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    # assert form_page.modal_dialog.exist()
    assert form_page.modal_dialog.not_exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerov')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.force_click()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies.force_click()
    form_page.current_address.send_keys('U.S., NY, Bairo de Lagoa st., 14')
    time.sleep(2)

    form_page.btn_submit.force_click()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.force_click()


def test_state_city_fields(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    time.sleep(2)
    form_page.input_state.send_keys('Haryana')
    form_page.input_state.send_keys(Keys.ENTER)

    form_page.btn_city.scroll_to_element()
    form_page.btn_city.click()
    time.sleep(2)
    form_page.input_city.send_keys(Keys.PAGE_DOWN)
    form_page.input_city.send_keys(Keys.ENTER)
