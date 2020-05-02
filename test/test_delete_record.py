import pytest
import allure
from api_requests.preconditions import Preconditions


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.account
@pytest.mark.delete
def test_delete_account(app):
    app.global_header.navigate_to_object('Account', 'Account')
    app.list_view_page.open_list_view('All Accounts')
    if not app.list_view_page.whether_record_exists('A8'):
        Preconditions().create_new_record(object_api_name='Account', record_type='0126F000001YvgZQAS',
                                          name='A8')
        app.refresh_the_page()
    app.list_view_page.delete_all_specified_records_and_verify('A8')


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.contact
@pytest.mark.delete
def test_delete_contact(app):
    app.global_header.navigate_to_object('Contact', 'Contact')
    app.list_view_page.open_list_view('All Contacts')
    app.list_view_page.delete_all_specified_records_and_verify('A8 contact')


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.delete
def test_delete_plastic_card(app):
    app.global_header.navigate_to_object('Plastic card', 'Plastic_card__c')
    app.list_view_page.open_list_view('All')
    app.list_view_page.delete_all_specified_records_and_verify('Visa8')
