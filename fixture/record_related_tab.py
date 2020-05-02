from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RecordRelatedTab:
    def __init__(self, app):
        self.app = app

    def expand_Show_more_actions_dropdown_on_record_page(self):
        driver = self.app.driver
        dropdown_locator = "//div[contains(@class,'windowViewMode-normal')]//span[contains(text(),'Show')]/.."
        dropdown_element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, dropdown_locator)))
        dropdown_element.click()

    def click_Edit_button(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//*[text()='Edit']/parent::a").click()

    def click_Edit_button_on_record_page(self):
        driver = self.app.driver
        # if "Edit" button is already displayed or not
        if len(driver.find_elements_by_xpath("//*[text()='Edit']/parent::a")):
            self.click_Edit_button()
        else:
            self.expand_Show_more_actions_dropdown_on_record_page()
            self.click_Edit_button()

    def check_that_page_title_contains_record_name(self, record_name):
        driver = self.app.driver
        print("\n" + driver.title)
        assert record_name in driver.title, "Wrong page title :)"

    def switch_to_Details_tab_of_record(self):
        driver = self.app.driver
        details_tab_element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                            "//div[contains(@class,'active')]//a[text()='Details']")))
        details_tab_element.click()
