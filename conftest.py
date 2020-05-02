from fixture.application_general import Application
import pytest
import json
import os.path
from parameters.sf_login_creds import SFLoginCreds

# store JSON as global variable
target_json = None


@pytest.fixture(scope="session")
def app(request):
    print("\nstart browser for test..")
    global target_json
    # read from command line or use default value
    browser_name = request.config.getoption("--browser")
    # read from JSON only once
    if target_json is None:
        # define the directory of the current file
        current_file_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_abs_path = os.path.join(current_file_dir, request.config.getoption("--target"))
        with open(config_file_abs_path) as config_file:
            target_json = json.load(config_file)
    fixture = Application(browser=browser_name, user_language=target_json['language'])
    fixture.login_page_sf.login_full(SFLoginCreds(username="ed@ed.ed", password="Cheglad3e|"))
    request.addfinalizer(fixture.quit_browser)
    return fixture


# add possibility to choose a browser when launching from command line
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="choose the browser: chrome or firefox")
    # parse parameters via JSON file
    parser.addoption("--target", action="store", default="target.json", help="choose a language: en, fr, es, ...etc")


@pytest.fixture(autouse=True)
def make_screenshot_and_refresh(request, app):
    tests_failed_before = request.session.testsfailed
    yield
    if request.session.testsfailed != tests_failed_before:
        test_name = request.node.name
        app.take_screenshot(test_name)
        app.refresh_the_page()
