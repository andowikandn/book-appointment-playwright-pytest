import allure
import pytest
from pages.login_pages import LoginPage
from pages.appointment_pages import AppointmentPage
from data.login import Username, Password

@allure.title('User login book appointment')
@allure.description('Do login with invalid and valid credentials')

def test_book_appointment_page(browser):
    homepage = AppointmentPage(browser)
    homepage.verify_home_page()

def test_login_page(browser):
    homepage = AppointmentPage(browser)
    login = LoginPage(browser)
    homepage.tap_appointment_btn()
    login.verify_login_page()

@pytest.mark.parametrize(
    "usernameInput, passwordInput", 
    [
        (Username.EMPTY, Password.EMPTY),
        (Username.INVALID, Password.INVALID),
        (Username.VALID, Password.INVALID),
        (Username.INVALID, Password.VALID)
    ]
)

def test_login_failed(usernameInput, passwordInput, browser):
    homepage = AppointmentPage(browser)
    login = LoginPage(browser)

    homepage.tap_appointment_btn()
    login.input_username(usernameInput)
    login.input_password(passwordInput)
    login.tap_login_btn()
    login.verify_login_error()

def test_login_success(browser):
    test_login_page(browser)
    login = LoginPage(browser)
    login.input_username(Username.VALID)
    login.input_password(Password.VALID)
    login.tap_login_btn()
    login.verify_login_success()