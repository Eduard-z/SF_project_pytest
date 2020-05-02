
class RecordDetailsTab:
    def __init__(self, app):
        self.app = app

    # data type - Text, Phone, Fax, Number, Percent, Picklist, Date, Time, Text Area, Long Text Area
    def check_text_value(self, field_name, field_value):
        driver = self.app.driver
        assert driver.find_element_by_xpath(f"//div[contains(@class, 'normal') and contains(@class, 'active')]"
                        f"//span[text()='{field_name}']/../following-sibling::div//*[text()='{field_value}']")

    def check_link_value(self, field_name, field_value):  # data type - Email, URL, Lookup
        driver = self.app.driver
        assert driver.find_element_by_xpath(
            f"//span[text()='{field_name}']/../following-sibling::div//a[text()='{field_value}']")

    def check_textarea_rich_value(self, field_name, field_value):
        driver = self.app.driver
        p_elements_list_element = driver.find_elements_by_xpath(
            f"//span[text()='{field_name}']/../following-sibling::div//p")
        field_value_split = field_value.split('\n')
        for i in range(len(field_value_split)):
            assert p_elements_list_element[i].text == field_value_split[i]

    def check_compound_value(self, field_name, field_value):  # data type - Currency, Picklist (Multi-Select)
        driver = self.app.driver
        assert driver.find_element_by_xpath(
            f"//span[text()='{field_name}']/../following-sibling::div//*[contains(text(),'{field_value}')]")

    def check_date_time_value(self, field_name, field_value_date, field_value_time):  # data type - Date/Time
        driver = self.app.driver
        assert driver.find_element_by_xpath(f"//span[text()='{field_name}']/../following-sibling::div"
                            f"//*[contains(text(),'{field_value_date}') and contains(text(),'{field_value_time}')]")

    def check_checkbox_value(self, field_name, checked):  # checked = "checked" or "unchecked"
        driver = self.app.driver
        assert driver.find_element_by_xpath(f"//div[contains(@class, 'normal') and contains(@class, 'active')]"
                                f"//span[text()='{field_name}']/../following-sibling::div//img[@class=' {checked}']")
