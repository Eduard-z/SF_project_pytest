from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from fixture.login_page_sf import LoginSalesforce

from fixture.global_header import GlobalHeader

from fixture.list_view_page import ListView
from fixture.record_modal_window import RecordModalWindow
from fixture.record_related_tab import RecordRelatedTab
from fixture.record_details_tab import RecordDetailsTab

from selenium.webdriver.chrome.options import Options
from datetime import datetime
import allure
from allure_commons.types import AttachmentType


class Application:
    def __init__(self, browser, user_language):
        desired_capabilites = None
        selenium_grid_url = "http://localhost:4444/wd/hub"

        # Create a desired capabilities object as a starting point.
        capabilities = DesiredCapabilities.CHROME.copy()
        # capabilities['platform'] = "WINDOWS"
        # capabilities['version'] = "10"

        # for Chrome
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        # for Firefox
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)

        if browser == "chrome":
            self.driver = webdriver.Chrome(options=options)
            # Instantiate an instance of Remote WebDriver with the desired capabilities
            # self.driver = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities=capabilities)
        elif browser == "firefox":
            self.driver = webdriver.Firefox(firefox_profile=fp)
        else:
            raise ValueError(f"Unrecognized browser {browser}")

        self.driver.implicitly_wait(5)
        self.login_page_sf = LoginSalesforce(self)

        self.global_header = GlobalHeader(self)

        self.list_view_page = ListView(self)
        self.record_modal_window = RecordModalWindow(self)
        self.record_related_tab = RecordRelatedTab(self)
        self.record_details_tab = RecordDetailsTab(self)

    def open_login_page(self):
        driver = self.driver
        driver.get("https://login.salesforce.com/")
        driver.maximize_window()

    def print_page_title(self):
        driver = self.driver
        print("\n" + driver.title)  # Lightning Experience

    def quit_browser(self):
        driver = self.driver
        print("\nquit browser..")
        driver.quit()

    def take_screenshot(self, test_name):
        driver = self.driver
        screenshots_dir = r"C:\Users\zakharove\PycharmProjects\SF_project_pytest\screenshots"
        test_time = str(datetime.now().strftime("%d-%m-%Y_T%H_%M_%S"))
        screenshot_file_path = f"{screenshots_dir}/{test_time} {test_name}.png"
        driver.save_screenshot(screenshot_file_path)
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{test_time} {test_name}",
                      attachment_type=AttachmentType.PNG)

    def refresh_the_page(self):
        driver = self.driver
        driver.refresh()
