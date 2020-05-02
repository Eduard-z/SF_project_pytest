from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class RecordModalWindow:
    def __init__(self, app):
        self.app = app

    def select_record_type_for_new_record(self, record_type_name):
        driver = self.app.driver
        record_type_radiobutton_element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                    f"//span[text()='{record_type_name}']/parent::div/preceding-sibling::div//span")))
        record_type_radiobutton_element.click()

    def click_Next_button_in_new_record_modal_window(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//span[text()='Next']").click()

    # data type - Text, Phone, Fax, Email, Currency, Number, Percent, URL
    def input_text_field(self, field_name, field_value):
        driver = self.app.driver
        field_element = driver.find_element_by_xpath(
            f"//div[contains(@class, 'modal')]//span[text()='{field_name}']/parent::label/following-sibling::input")
        field_element.clear()
        field_element.send_keys(field_value)

    def input_percent_field(self, field_name, field_value):
        driver = self.app.driver
        field_element = driver.find_element_by_xpath(
            f"//div[contains(@class, 'modal')]//span[text()='{field_name}']/parent::label/following-sibling::input")
        hovering = ActionChains(driver)
        hovering.move_to_element(field_element).double_click().perform()
        field_element.send_keys(field_value)

    def input_picklist_field(self, field_name, field_value):  # data type - Picklist
        driver = self.app.driver
        driver.find_element_by_xpath(f"//span[text()='{field_name}']/parent::span/following-sibling::div//a").click()
        driver.find_element_by_xpath(f"//a[@title='{field_value}']").click()

    def input_picklist_multiselect_field(self, field_name, field_value):  # data type - Picklist (Multi-Select)
        driver = self.app.driver
        picklist_multiselect_value_element = driver.find_element_by_xpath(
            f"//div[text()='{field_name}']/following-sibling::div//span[text()='Available']"
            f"/following-sibling::div//span[text()='{field_value}']")
        hovering = ActionChains(driver)
        hovering.move_to_element(picklist_multiselect_value_element).click().perform()
        picklist_move_forward_arrow_element = driver.find_element_by_xpath(
            f"//div[text()='{field_name}']/following-sibling::div//button[@title='Move selection to Chosen']")
        hovering.move_to_element(picklist_move_forward_arrow_element).click().perform()

    def remove_picklist_multiselect_field(self, field_name, field_value):  # data type - Picklist (Multi-Select)
        driver = self.app.driver
        picklist_multiselect_value_element = driver.find_element_by_xpath(
            f"//div[text()='{field_name}']/following-sibling::div//span[text()='Chosen']"
            f"/following-sibling::div//span[text()='{field_value}']")
        hovering = ActionChains(driver)
        hovering.move_to_element(picklist_multiselect_value_element).click().perform()
        picklist_move_back_arrow_element = driver.find_element_by_xpath(
                f"//div[text()='{field_name}']/following-sibling::div//button[@title='Move selection to Available']")
        hovering.move_to_element(picklist_move_back_arrow_element).click().perform()

    def input_date_field(self, field_name, field_value):  # data type - Date
        driver = self.app.driver
        field_locator = f"//span[text()='{field_name}']/parent::label/following-sibling::div//input"
        driver.find_element_by_xpath(field_locator).clear()
        driver.find_element_by_xpath(field_locator).send_keys(field_value)

    def input_time_field(self, field_name, field_value):  # data type - Time
        driver = self.app.driver
        field_locator = f"//label[text()='{field_name}']/following-sibling::div//input"
        driver.find_element_by_xpath(field_locator).clear()
        driver.find_element_by_xpath(field_locator).send_keys(field_value)

    def input_date_time_field(self, field_name, field_value_date, field_value_time):  # data type - Date/Time
        driver = self.app.driver
        date_field_locator = f"//span[text()='{field_name}']/parent::legend/following-sibling::div//" \
                             f"label[text()='Date']/following-sibling::input"
        time_field_locator = f"//span[text()='{field_name}']/parent::legend/following-sibling::div//" \
                             f"label[text()='Time']/following-sibling::input"
        # populate time, then date
        driver.find_element_by_xpath(time_field_locator).clear()
        driver.find_element_by_xpath(time_field_locator).clear()
        driver.find_element_by_xpath(time_field_locator).send_keys(field_value_time)
        driver.find_element_by_xpath(date_field_locator).clear()
        driver.find_element_by_xpath(date_field_locator).send_keys(field_value_date)

    def input_checkbox_field(self, field_name, checked):  # checked = "checked" or "unchecked"
        driver = self.app.driver
        checkbox_locator = f"//div[contains(@class, 'modal')]" \
                           f"//span[text()='{field_name}']/parent::label/following-sibling::input"
        checkbox_element = driver.find_element_by_xpath(checkbox_locator)
        checkbox_value = checkbox_element.get_attribute("checked")
        if (checked == "checked" and checkbox_value is None) or (checked == "unchecked" and checkbox_value == "true"):
            checkbox_element.click()

    def input_textarea_field(self, field_name, field_value):  # data type - Text Area, Long Text Area
        driver = self.app.driver
        field_locator = f"//span[text()='{field_name}']/parent::label/following-sibling::textarea"
        driver.find_element_by_xpath(field_locator).clear()
        driver.find_element_by_xpath(field_locator).send_keys(field_value)

    def input_textarea_rich_field(self, field_name, field_value):  # data type - Rich Text Area
        driver = self.app.driver
        field_locator = f"//span[text()='{field_name}']/following-sibling::div/div[@role]/following-sibling::div/div"
        driver.find_element_by_xpath(field_locator).clear()
        driver.find_element_by_xpath(field_locator).send_keys(field_value)

    def input_lookup_field(self, field_name, field_value):  # data type - Lookup
        driver = self.app.driver
        driver.find_element_by_xpath(f"//span[text()='{field_name}']/parent::label/following-sibling::div//input").\
            send_keys(field_value)
        # choose any record that matches by name
        driver.find_element_by_xpath(f"//span[text()='{field_name}']"
                                     f"/parent::label/following-sibling::div//*[@title='{field_value}']").click()

    def remove_lookup_field_value(self, field_name):  # data type - Lookup
        driver = self.app.driver
        driver.find_element_by_xpath(f"//span[text()='{field_name}']/parent::label/following-sibling::div"
                                     f"//span[text()='Press Delete to Remove']/parent::a").click()

    def click_Save_button(self):
        driver = self.app.driver
        button_save_locator = "//button[@title='Save']//span[text()='Save']"
        driver.find_element_by_xpath(button_save_locator).click()
        # verify that modal window is closed
        WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.XPATH, button_save_locator)))

    def click_Delete_button_inside_confirmation_window(self):
        driver = self.app.driver
        button_delete_element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                            "//h2[contains(text(),'Delete')]/../following-sibling::*//button//span[text()='Delete']")))
        button_delete_element.click()
        print("record deleted")
