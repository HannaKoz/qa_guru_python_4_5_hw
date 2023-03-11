import pytest
from selene import browser
from selene.support.shared import browser

@pytest.fixture()
def browser_size_w1920_h1080():
    #browser.config.browser_name = "Firefox"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser_size_w1920_h1080
    browser.config.hold_browser_open = True

@pytest.fixture()
def browser_size_w1280_h720():
    #browser.config.browser_name = "Firefox"
    browser.config.window_width = 1280
    browser.config.window_height = 720
