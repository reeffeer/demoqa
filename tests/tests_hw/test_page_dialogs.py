from conftest import browser
from pages.modal_dialogs import ModalDialogs


def test_modal_dialogs(browser):
    modal_dialogs_page = ModalDialogs(browser)

    modal_dialogs_page.visit()
    modal_dialogs_page.submenu_btns.check_count_elements(5)


def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)

    modal_dialogs_page.visit()
    modal_dialogs_page.refresh()
    modal_dialogs_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert browser.current_url == 'https://demoqa.com/'
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
