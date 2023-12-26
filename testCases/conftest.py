from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser..........")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser.........")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############### PyTest HTML Report ##############


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'inmvc'
        config._metadata['Module Name'] = 'Login'
        config._metadata['Tester'] = 'Krishna'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
