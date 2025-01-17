import time

import pytest
from selenium.webdriver import Keys

from conftest import browser
from pages.slider import Slider


@pytest.mark.smoke
def test_slider(browser):
    slider = Slider(browser)
    slider.visit()

    assert slider.slider.exist()
    assert slider.slider_input.exist()

    while not slider.slider_input.get_dom_attribute('value') == '50':
        slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider.slider_input.get_dom_attribute('value') == '50'
