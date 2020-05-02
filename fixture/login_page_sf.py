
class LoginSalesforce:
    def __init__(self, app):
        self.app = app

    def log_into_org(self, creds):
        driver = self.app.driver
        if creds.username is not None:
            driver.find_element_by_id("username").send_keys(creds.username)
        if creds.password is not None:
            driver.find_element_by_id("password").send_keys(creds.password)
        driver.find_element_by_id("Login").click()

    def check_if_login_window_is_displayed(self):
        driver = self.app.driver
        # if driver.title.startswith("Choose a Username"): # check page title
        # if driver.find_element_by_id("use_new_identity_div").get_attribute("style") != "display: none;": # check attr
        link_to_login_window_element = driver.find_element_by_id("use_new_identity")
        if link_to_login_window_element.is_displayed():  # if element is displayed
            link_to_login_window_element.click()

    def verify_login_wrong_password_error_message(self):
        driver = self.app.driver
        assert driver.find_element_by_id('error').text == \
            "Please check your username and password. If you still can't log in, contact your Salesforce administrator."

    def verify_login_without_password_error_message(self):
        driver = self.app.driver
        assert driver.find_element_by_id('error').text == "Please enter your password."

    def login_full(self, creds):
        self.app.open_login_page()
        self.check_if_login_window_is_displayed()
        self.log_into_org(creds)
        self.app.print_page_title()
