import time

import pytest
from selenium import webdriver

from pages.web_tables import WebTables


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 1000)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def add_rows(browser):
    page = WebTables(browser)
    page.visit()

    page.rows_per_page.click()
    page.rows_per_page.select_by_index(0)

    page.btn_add.click()
    assert page.reg_form.exist()
    page.first_name.send_keys('Abs')
    page.last_name.send_keys('Crabs')
    page.email.send_keys('lf@gt.ti')
    page.age.send_keys(32)
    page.salary.send_keys(98000)
    page.department.send_keys('Bio')
    page.btn_submit.click()
    time.sleep(2)

    page.btn_add.click()
    assert page.reg_form.exist()
    page.first_name.send_keys('See')
    page.last_name.send_keys('More')
    page.email.send_keys('rout@gata.ml')
    page.age.send_keys(27)
    page.salary.send_keys(101)
    page.department.send_keys('goods')
    page.btn_submit.click()
    time.sleep(2)
