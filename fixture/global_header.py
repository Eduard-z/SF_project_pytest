from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GlobalHeader:
    def __init__(self, app):
        self.app = app

    def click_App_Launcher_icon(self):
        driver = self.app.driver
        app_launcher_element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                    "//span[text()='App Launcher']/..")))
        app_launcher_element.click()

    def input_object_name_into_apps_and_items_search(self, object_name):
        driver = self.app.driver
        search_field_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                            "//input[@type='search' and @placeholder='Search apps and items...']")))
        search_field_element.clear()
        search_field_element.send_keys(object_name)  # object name in singular (good only for standard objects)

    def hover_object_name_into_apps_and_items_search_then_click(self, object_api_name):
        driver = self.app.driver
        # hover an element
        target_item_element = driver.find_element_by_xpath(f"//a[@id='{object_api_name}']")
        hovering = ActionChains(driver)
        hovering.move_to_element(target_item_element).click().perform()

    def navigate_to_object(self, object_name, object_api_name):
        self.click_App_Launcher_icon()
        self.input_object_name_into_apps_and_items_search(object_name)
        self.hover_object_name_into_apps_and_items_search_then_click(object_api_name)
        self.app.list_view_page.wait_until_an_object_list_view_is_displayed(object_name)
