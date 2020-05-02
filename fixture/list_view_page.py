from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class ListView:
    def __init__(self, app):
        self.app = app

    def wait_until_an_object_list_view_is_displayed(self, object_name):
        driver = self.app.driver
        WebDriverWait(driver, 10).until(EC.title_contains(object_name))

    def create_record_click_new_button(self):
        driver = self.app.driver
        button_new_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "//div[text()='New' and @title='New']")))
        button_new_element.click()

    def expand_list_view_dropdown(self):
        driver = self.app.driver
        list_view_dropdown_element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                    "//a[@title='Select List View']")))
        list_view_dropdown_element.click()

    def select_list_view(self, list_view_name):
        driver = self.app.driver
        list_view_name_locator = f"//span[text()='{list_view_name}']/parent::a"
        driver.find_element_by_xpath(list_view_name_locator).click()

    def search_the_record_on_the_list(self, record_name):
        driver = self.app.driver
        record_name_locator = f"//a[text()='{record_name}' and @title='{record_name}']"
        if len(driver.find_elements_by_xpath(record_name_locator)) == 0:
            search_field_element = driver.find_element_by_xpath("//input[@placeholder='Search this list...']")
            # input record name into search field and press [Enter]
            search_field_element.send_keys(f"{record_name}")
            search_field_element.send_keys(Keys.ENTER)

    def whether_record_exists(self, record_name):
        driver = self.app.driver
        self.wait_until_the_list_of_records_is_refreshed()
        record_name_locator = f"//a[text()='{record_name}' and @title='{record_name}']"
        self.search_the_record_on_the_list(record_name)
        return len(driver.find_elements_by_xpath(record_name_locator))

    def click_record_name(self, record_name):
        driver = self.app.driver
        self.wait_until_the_list_of_records_is_refreshed()
        record_name_locator = f"//a[text()='{record_name}' and @title='{record_name}']"
        self.search_the_record_on_the_list(record_name)
        # click first record name
        driver.find_elements_by_xpath(record_name_locator)[0].click()

    def click_Delete_button_inside_dropdown(self):
        driver = self.app.driver
        button_delete_element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                           "//a[@title='Delete']")))
        button_delete_element.click()

    def check_all_records_deleted(self, record_name):
        driver = self.app.driver
        assert len(driver.find_elements_by_xpath(f"//a[text()='{record_name}' and @title='{record_name}']")) == 0

    def wait_until_the_list_of_records_is_refreshed(self):
        driver = self.app.driver
        WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.XPATH,
                                            "//*[text()='Refresh this list to view the latest data']")))

    def delete_all_specified_records_and_verify(self, record_name):
        driver = self.app.driver
        record_name_locator = f"//a[text()='{record_name}' and @title='{record_name}']"
        while self.whether_record_exists(record_name):
            self.search_the_record_on_the_list(record_name)
            # expand drop-down with actions
            driver.find_element_by_xpath(
                f"{record_name_locator}/ancestor::tr//td//a[@role='button']").click()
            self.click_Delete_button_inside_dropdown()
            # confirm deleting
            self.app.record_modal_window.click_Delete_button_inside_confirmation_window()
            self.wait_until_the_list_of_records_is_refreshed()
        self.check_all_records_deleted(record_name)

    def open_list_view(self, list_view_name):
        self.expand_list_view_dropdown()
        self.select_list_view(list_view_name)
