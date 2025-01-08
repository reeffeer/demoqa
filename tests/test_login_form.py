import time

from conftest import browser
from pages.form_page import FormPage


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerov')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.force_click()
    form_page.user_number.send_keys('9992223344')
    time.sleep(2)
    form_page.btn_submit.force_click()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.force_click()
