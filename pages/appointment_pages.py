import allure
from locators.appointment_locator import AppointmentLocator   
from playwright.sync_api import Page, expect

class AppointmentPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_home_page(self):
        with allure.step('Verify home page'):
            expect(self.page.locator(AppointmentLocator.homepage_header)).to_be_visible()
            expect(self.page.locator(AppointmentLocator.homepage_header)).to_have_text('CURA Healthcare Service')
            expect(self.page).to_have_url("https://katalon-demo-cura.herokuapp.com/")

    def tap_appointment_btn(self):
        with allure.step('User make appointment'):
            self.page.locator(AppointmentLocator.make_appoinment_btn).click()

    def select_facility(self, facility_option: str):
        with allure.step(f'View option facility: {facility_option}'):
            self.page.locator(AppointmentLocator.facility_option).select_option(label=facility_option)
    
    def checked_facility(self):
        with allure.step('User checked facility'):
            self.page.locator(AppointmentLocator.checkbox_facility).check()
    
    def select_program_health(self, select_program: str):
        with allure.step(f'User select program health: {select_program}'):
            self.page.locator(f'{AppointmentLocator.program_health_option}[value="{select_program}"]').check()

    def input_visit_date(self, select_date: str):
        with allure.step(f'user input visit date: {select_date}'):
            locator = self.page.locator(AppointmentLocator.visit_date)
            expect(locator).to_be_visible()
            locator.click()
            locator.fill('')
            locator.press_sequentially(select_date)
            expect(locator).to_have_value(select_date)

    def input_comment(self, comment: str):
        with allure.step(f'User input text comment: {comment}'):
            self.page.locator(AppointmentLocator.comment_field).fill(comment)
    
    def tap_book_appointment(self):
        with allure.step('User click book appointment button'):
            self.page.locator(AppointmentLocator.book_apppoinment_btn).click()

    def verify_book_appointment(self):
        with allure.step('Verify book appointment success'):
            expect(self.page.locator(AppointmentLocator.confirmation_page)).to_be_visible(timeout=10000)
            expect(self.page).to_have_url('https://katalon-demo-cura.herokuapp.com/appointment.php#summary', timeout=10000)
            expect(self.page.locator(AppointmentLocator.comment_confirm_txt)).to_be_visible(timeout=10000)
            print("Current Url:", self.page.url)

    def tap_homepage_btn(self):
        with allure.step('User click Go to Homepage'):
            self.page.locator(AppointmentLocator.homepage_btn).click()