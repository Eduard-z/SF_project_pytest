from pytest_bdd import given, when, then


@given('list view of Account object <object_name> <object_api_name>')
def navigate_to_account_object(app, object_name, object_api_name):
    app.global_header.navigate_to_object(object_name, object_api_name)


@when('I open New Account modal form for <record_type_name>')
def open_modal_form_for_new_record(app, record_type_name):
    app.list_view_page.create_record_click_new_button()
    app.record_modal_window.select_record_type_for_new_record(record_type_name)
    app.record_modal_window.click_Next_button_in_new_record_modal_window()


@when('I populate <field_1> with <field_1_value>')
def populate_field_1(app, field_1, field_1_value):
    app.record_modal_window.input_text_field(field_1, field_1_value)


@when('I populate <field_2> with <field_2_value>')
def populate_field_1(app, field_2, field_2_value):
    app.record_modal_window.input_picklist_field(field_2, field_2_value)


@when('I populate <field_3> with <field_3_value>')
def populate_field_1(app, field_3, field_3_value):
    app.record_modal_window.input_checkbox_field(field_3, field_3_value)


@when('I click "Save" button')
def save_new_record(app):
    app.record_modal_window.click_Save_button()


@then('new Account record is created')
def check_that_page_title_contains_record_name(app, field_1_value):
    app.record_related_tab.switch_to_Details_tab_of_record()
    app.record_related_tab.check_that_page_title_contains_record_name(field_1_value)


@then('having <field_1> equal to <field_1_value>')
def check_field_1_value(app, field_1, field_1_value):
    app.record_details_tab.check_text_value(field_1, field_1_value)


@then('having <field_2> equal to <field_2_value>')
def check_field_2_value(app, field_2, field_2_value):
    app.record_details_tab.check_text_value(field_2, field_2_value)


@then('having <field_3> equal to <field_3_value>')
def check_field_3_value(app, field_3, field_3_value):
    app.record_details_tab.check_checkbox_value(field_3, field_3_value)
