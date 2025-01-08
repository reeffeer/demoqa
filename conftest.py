import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.fullscreen_window()
    yield driver
    driver.quit()
