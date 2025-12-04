import allure
from locators.login_locator import LoginLocator
from locators.appointment_locator import AppointmentLocator
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_login_page(self):
        with allure.step('Verify login page'):
            expect(self.page.locator(LoginLocator.login_page)).to_be_visible()
            expect(self.page.locator('p.lead')).to_have_text('Please login to make appointment.')
            expect(self.page).to_have_url('https://katalon-demo-cura.herokuapp.com/profile.php#login')

    def input_username(self, username: str):
        with allure.step('User input username'):
            self.page.locator(LoginLocator.username_txt).fill(username)
            
    def input_password(self, password: str):
        with allure.step('User input password'):
            self.page.locator(LoginLocator.password_txt).fill(password)

    def tap_login_btn(self):
        with allure.step('Input click login'):
            self.page.locator(LoginLocator.login_btn).click()

    def verify_login_error(self):
        with allure.step('Verify login error message'):
            expect(self.page.locator(LoginLocator.login_err_msg)).to_be_visible()
            expect(self.page.locator(LoginLocator.login_err_msg)).to_have_text('Login failed! Please ensure the username and password are valid.')

    def verify_login_success(self):
        with allure.step('Verify login success'):
            expect(self.page.locator(AppointmentLocator.login_success)).to_be_visible()
            expect(self.page).to_have_url('https://katalon-demo-cura.herokuapp.com/#appointment')