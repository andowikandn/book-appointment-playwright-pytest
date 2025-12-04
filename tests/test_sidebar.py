import allure
from pages.login_pages import LoginPage
from pages.appointment_pages import AppointmentPage
from pages.sidebar_pages import SidebarPage

@allure.title('User view sidebar menu')
@allure.description('Do action sidebar menut')

def test_sidebar_menu(browser):
    sidebar = SidebarPage(browser)
    login = LoginPage(browser)
    appointment = AppointmentPage(browser)
    appointment.tap_appointment_btn()
    login.input_username('John Doe')
    login.input_password('ThisIsNotAPassword')
    login.tap_login_btn()
    sidebar.tap_sidebar_menu()
    sidebar.verify_sidebar_menu()

def test_sidebar_history_page(browser):
    test_sidebar_menu(browser)
    sidebar = SidebarPage(browser)
    sidebar.tap_history_menu()
    sidebar.verify_history_page()

def test_sidebar_profile_page(browser):
    test_sidebar_menu(browser)
    sidebar = SidebarPage(browser)
    sidebar.tap_profile_menu()
    sidebar.verify_profile_page()

def test_user_logout(browser):
    test_sidebar_menu(browser)
    sidebar = SidebarPage(browser)
    sidebar.tap_logout_menu()
    sidebar.verify_success_logout()