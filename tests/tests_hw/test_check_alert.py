from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import browser
from pages.alerts import Alerts


def test_alert_time(browser):
    alerts_page = Alerts(browser)
    alerts_page.visit()

    assert not alerts_page.alert()
    alerts_page.timer_alert_btn.click()
    WebDriverWait(browser, 6).until(expected_conditions.alert_is_present())
    assert alerts_page.alert() is not None
