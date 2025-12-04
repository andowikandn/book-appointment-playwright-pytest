import allure
from locators.sidebar_locator import SidebarLocator
from locators.appointment_locator import AppointmentLocator
from playwright.sync_api import Page, expect

class SidebarPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_sidebar_menu(self):
        with allure.step('Verfiy sidebar menu page'):
            expect(self.page.locator(SidebarLocator.sidebar_page)).to_be_visible()
    
    def tap_sidebar_menu(self):
        with allure.step('User click sidebar menu'):
            self.page.locator(SidebarLocator.toogle_menu).click()
    
    def tap_history_menu(self):
        with allure.step('User click history menu'):
            self.page.locator(SidebarLocator.sidebar_history).click()

    def verify_history_book_appointment(self):
        with allure.step('Verify history with book appoinment'):
            expect(self.page.locator(SidebarLocator.history_page)).to_be_visible()
            expect(self.page).to_have_url('https://katalon-demo-cura.herokuapp.com/history.php#history', timeout=10000)
            expect(self.page.locator(SidebarLocator.hospital_readmission)).to_be_visible()

    def verify_history_page(self):
        with allure.step('Verify history page appoinment'):
            expect(self.page.locator(SidebarLocator.history_page)).to_be_visible()
            expect(self.page).to_have_url('https://katalon-demo-cura.herokuapp.com/history.php#history', timeout=10000)

    def tap_profile_menu(self):
        with allure.step('User click profile menu'):
            self.page.locator(SidebarLocator.sidebar_profile).click()

    def verify_profile_page(self):
        with allure.step('Verify profile page'):
            expect(self.page.locator(SidebarLocator.profile_page)).to_be_visible()
            expect(self.page).to_have_url('https://katalon-demo-cura.herokuapp.com/profile.php#profile', timeout=10000)

    def tap_logout_menu(self):
        with allure.step('User click logout menu'):
            self.page.locator(SidebarLocator.sidebar_logout).click()
    
    def verify_success_logout(self):
        with allure.step('Verify user success logout'):
            expect(self.page.locator(AppointmentLocator.homepage_header)).to_be_visible()
            expect(self.page.locator(AppointmentLocator.homepage_header)).to_have_text('CURA Healthcare Service')
            assert self.page.url == 'https://katalon-demo-cura.herokuapp.com/'