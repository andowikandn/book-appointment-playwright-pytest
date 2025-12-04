import allure
import pytest
from pages.login_pages import LoginPage
from pages.appointment_pages import AppointmentPage

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

invalid_credentials = [
    ('',''),
    ('typo','typo'),
    ('John Doe',''),
    ('','ThisIsNotAPassword')
    ]

@pytest.mark.parametrize('username, password', invalid_credentials)
def test_login_failed(username, password, browser):
    homepage = AppointmentPage(browser)
    login = LoginPage(browser)
    homepage.tap_appointment_btn()
    login.input_username(username)
    login.input_password(password)
    login.tap_login_btn()
    login.verify_login_error()

def test_login_success(browser):
    test_login_page(browser)
    login = LoginPage(browser)
    login.input_username('John Doe')
    login.input_password('ThisIsNotAPassword')
    login.tap_login_btn()
    login.verify_login_success()