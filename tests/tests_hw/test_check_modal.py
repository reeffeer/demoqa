import time
import pytest
import requests

from conftest import browser
from pages.modal_dialogs import ModalDialogs


def check_url(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


@pytest.mark.skipif(not check_url("https://demoqa.com/modal-dialogs"), reason="Page is not available")
def test_modal_buttons(browser):
    modal = ModalDialogs(browser)
    modal.visit()

    assert modal.showSmallModal.exist()
    assert modal.showLargeModal.exist()

    modal.showSmallModal.click()
    time.sleep(2)
    assert modal.closeSmallModal.exist()
    modal.closeSmallModal.click()
    time.sleep(2)
    assert not modal.alert()

    modal.showLargeModal.click()
    time.sleep(2)
    assert modal.closeLargeModal.exist()
    modal.closeLargeModal.click()
    time.sleep(2)
    assert not modal.alert()
