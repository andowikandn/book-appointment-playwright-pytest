import allure
import json
from pages.appointment_pages import AppointmentPage
from pages.sidebar_pages import SidebarPage
from pages.login_pages import LoginPage
from data.login import Username, Password
from data.form import Facility, HealthProgram, VisitDate, Comment

@allure.title('User fill form book appointment')
@allure.description('Do input appoinment program health care')

def test_input_book_appointment_form(browser):
    appointment = AppointmentPage(browser)
    login = LoginPage(browser)
    appointment.tap_appointment_btn()
    login.input_username(Username.VALID)
    login.input_password(Password.VALID)
    login.tap_login_btn()
    appointment.select_facility(Facility.HONGKONG)
    appointment.checked_facility()
    appointment.select_program_health(HealthProgram.MEDICARE)
    appointment.input_visit_date(VisitDate.DATE)
    appointment.input_comment(Comment.TEXT)
    appointment.tap_book_appointment()
    appointment.verify_book_appointment()

def test_history_book_appointment(browser):
    test_input_book_appointment_form(browser)
    sidebar = SidebarPage(browser)
    sidebar.tap_sidebar_menu()
    sidebar.tap_history_menu()
    sidebar.verify_history_book_appointment()

def test_tap_homepage_btn(browser):
    test_input_book_appointment_form(browser)
    appointment = AppointmentPage(browser)
    appointment.tap_homepage_btn()
    appointment.verify_home_page()