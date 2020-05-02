import pytest
import allure
from api_requests.preconditions import Preconditions


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.account
@pytest.mark.edit
def test_edit_account(app):
    app.global_header.navigate_to_object('Account', 'Account')
    app.list_view_page.open_list_view('All Accounts')
    if not app.list_view_page.whether_record_exists('A8'):
        Preconditions().create_new_record(object_api_name='Account', record_type='0126F000001YvgZQAS',
                                          name='A8')
        app.refresh_the_page()
    app.list_view_page.click_record_name('A8')
    app.record_related_tab.click_Edit_button_on_record_page()
    app.record_modal_window.input_text_field('Phone', '+36985214700')
    app.record_modal_window.input_picklist_field('Prospect Rating', 'Cold')
    app.record_modal_window.click_Save_button()
    app.record_related_tab.switch_to_Details_tab_of_record()
    app.record_details_tab.check_text_value('Phone', '+36985214700')
    app.record_details_tab.check_text_value('Prospect Rating', 'Cold')


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.contact
@pytest.mark.edit
def test_edit_contact(app):
    app.global_header.navigate_to_object('Contact', 'Contact')
    app.list_view_page.open_list_view('All Contacts')
    app.list_view_page.click_record_name('A8 contact')
    app.record_related_tab.click_Edit_button_on_record_page()
    app.record_modal_window.input_text_field('Phone', '+36985214700')
    app.record_modal_window.input_picklist_field('Lead Source', 'Phone Inquiry')
    app.record_modal_window.remove_picklist_multiselect_field('MultiSelect for test', 'second')
    app.record_modal_window.input_picklist_multiselect_field('MultiSelect for test', 'first')
    app.record_modal_window.input_date_field('Birthdate', '05/02/2003')
    app.record_modal_window.input_time_field('Time for test', '13:06')
    app.record_modal_window.input_date_time_field('DateTime for test', '05/02/2003', '02:51')
    app.record_modal_window.input_percent_field('Percent for test', '37')
    app.record_modal_window.input_checkbox_field('Prequalified?', 'unchecked')
    app.record_modal_window.input_textarea_field('Description', 'qwer')
    app.record_modal_window.input_textarea_rich_field('Textarea Rich', 'a\ns\nd\n0')
    app.record_modal_window.remove_lookup_field_value('Account Name')
    app.record_modal_window.input_lookup_field('Account Name', 'client_1')
    app.record_modal_window.click_Save_button()
    app.record_related_tab.switch_to_Details_tab_of_record()
    app.record_details_tab.check_text_value('Phone', '+36985214700')
    app.record_details_tab.check_text_value('Percent for test', '37%')
    app.record_details_tab.check_text_value('Description', 'qwer')
    app.record_details_tab.check_textarea_rich_value('Textarea Rich', 'a\ns\nd\n0')
    app.record_details_tab.check_compound_value('MultiSelect for test', 'first')
    app.record_details_tab.check_text_value('Lead Source', 'Phone Inquiry')
    app.record_details_tab.check_text_value('Birthdate', '05/02/2003')
    app.record_details_tab.check_text_value('Time for test', '13:06')
    app.record_details_tab.check_date_time_value('DateTime for test', '05/02/2003', '02:51')
    # app.record_details_tab.check_checkbox_value('Prequalified?', 'unchecked')
    app.record_details_tab.check_link_value('Account Name', 'client_1')


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.edit
def test_edit_plastic_card(app):
    app.global_header.navigate_to_object('Plastic card', 'Plastic_card__c')
    app.list_view_page.open_list_view('All')
    app.list_view_page.click_record_name('Visa8')
    app.record_related_tab.click_Edit_button_on_record_page()
    app.record_modal_window.input_text_field('Plastic card Name', 'Visa2_A')
    app.record_modal_window.input_picklist_field('Plastic card type', 'MasterCard')
    app.record_modal_window.click_Save_button()
    app.record_related_tab.switch_to_Details_tab_of_record()
    app.record_details_tab.check_text_value('Plastic card Name', 'Visa2_A')
    app.record_details_tab.check_text_value('Plastic card type', 'MasterCard')
