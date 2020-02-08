import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome(executable_path='d:\\PycharmProjects\\HW-Elements_searching\\drivers\\chromedriver.exe')
    return browser
