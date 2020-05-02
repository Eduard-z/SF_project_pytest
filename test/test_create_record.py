import pytest
import allure


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.account
@pytest.mark.create
def test_create_account(app):
    app.global_header.navigate_to_object('Account', 'Account')
    app.list_view_page.create_record_click_new_button()
    app.record_modal_window.select_record_type_for_new_record('Organization')
    app.record_modal_window.click_Next_button_in_new_record_modal_window()
    app.record_modal_window.input_text_field('Account Name', 'A8')
    app.record_modal_window.input_picklist_field('Prospect Rating', 'Warm')
    app.record_modal_window.input_date_field('Support Plan Expiration Date', '05/02/2002')
    app.record_modal_window.input_checkbox_field('Has Support Plan', 'checked')
    app.record_modal_window.click_Save_button()
    app.record_related_tab.switch_to_Details_tab_of_record()
    app.record_related_tab.check_that_page_title_contains_record_name('A8')
    app.record_details_tab.check_text_value('Account Name', 'A8')
    app.record_details_tab.check_text_value('Prospect Rating', 'Warm')
    app.record_details_tab.check_text_value('Support Plan Expiration Date', '05/02/2002')
    # app.record_details_tab.check_checkbox_value('Has Support Plan', 'checked')


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.contact
@pytest.mark.create
def test_create_contact(app):
    app.global_header.navigate_to_object('Contact', 'Contact')
    app.list_view_page.create_record_click_new_button()
    app.record_modal_window.select_record_type_for_new_record('Fin. Director')
    app.record_modal_window.click_Next_button_in_new_record_modal_window()
    app.record_modal_window.input_text_field('Last Name', 'A8 contact')
    app.record_modal_window.input_percent_field('Percent for test', '75')
    app.record_modal_window.input_textarea_field('Description', '1234')
    app.record_modal_window.input_textarea_rich_field('Textarea Rich', '1\n2\n3\n4')
    app.record_modal_window.input_picklist_multiselect_field('MultiSelect for test', 'second')
    app.record_modal_window.input_picklist_field('Lead Source', 'Partner Referral')
    app.record_modal_window.input_date_field('Birthdate', '05/02/2002')
    app.record_modal_window.input_time_field('Time for test', '01:49')
    app.record_modal_window.input_date_time_field('DateTime for test', '05/02/2002', '14:18')
    app.record_modal_window.input_checkbox_field('Prequalified?', 'checked')
    app.record_modal_window.input_lookup_field('Account Name', 'A8')
    app.record_modal_window.click_Save_button()
    app.record_related_tab.switch_to_Details_tab_of_record()
    app.record_related_tab.check_that_page_title_contains_record_name('A8 contact')
    app.record_details_tab.check_text_value('Name', 'A8 contact')
    app.record_details_tab.check_text_value('Percent for test', '75%')
    app.record_details_tab.check_text_value('Description', '1234')
    app.record_details_tab.check_textarea_rich_value('Textarea Rich', '1\n2\n3\n4')
    app.record_details_tab.check_compound_value('MultiSelect for test', 'second')
    app.record_details_tab.check_text_value('Lead Source', 'Partner Referral')
    app.record_details_tab.check_text_value('Birthdate', '05/02/2002')
    app.record_details_tab.check_text_value('Time for test', '01:49')
    app.record_details_tab.check_date_time_value('DateTime for test', '05/02/2002', '14:18')
    # app.record_details_tab.check_checkbox_value('Prequalified?', 'checked')
    app.record_details_tab.check_link_value('Account Name', 'A8')


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.create
def test_create_plastic_card(app):
    app.global_header.navigate_to_object('Plastic card', 'Plastic_card__c')
    app.list_view_page.create_record_click_new_button()
    app.record_modal_window.select_record_type_for_new_record('Visa')
    app.record_modal_window.click_Next_button_in_new_record_modal_window()
    app.record_modal_window.input_text_field('Plastic card Name', 'Visa8')
    app.record_modal_window.input_picklist_field('Plastic card type', 'Visa')
    app.record_modal_window.input_checkbox_field('isActive', 'checked')
    app.record_modal_window.input_lookup_field('Bank Account', 'acc# 0004')
    app.record_modal_window.click_Save_button()
    app.record_related_tab.switch_to_Details_tab_of_record()
    app.record_related_tab.check_that_page_title_contains_record_name('Visa8')
    app.record_details_tab.check_text_value('Plastic card Name', 'Visa8')
    app.record_details_tab.check_text_value('Plastic card type', 'Visa')
    # app.record_details_tab.check_checkbox_value('isActive', 'checked')
    app.record_details_tab.check_link_value('Bank Account', 'acc# 0004')
