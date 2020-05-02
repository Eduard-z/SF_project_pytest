from parameters.sf_login_creds import SFLoginCreds
import pytest
from data.login_creds_wrong import test_login_creds


@pytest.mark.skip
@pytest.mark.login
@pytest.mark.parametrize("test_creds", test_login_creds, ids=[repr(x) for x in test_login_creds])
def test_login_with_incorrect_password(app, test_creds):
    app.login_page_sf.login_full(test_creds)
    app.login_page_sf.verify_login_wrong_password_error_message()


@pytest.mark.skip
@pytest.mark.login
def test_login_without_entering_password(app):
    app.login_page_sf.login_full(SFLoginCreds(username="ed@ed.ed", password=""))
    app.login_page_sf.verify_login_without_password_error_message()
