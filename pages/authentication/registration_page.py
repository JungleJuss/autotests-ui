from playwright.sync_api import  Page

from components.authentification.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
import re



class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration button')
        self.login_button = Link(page, 'registration-page-login-link', 'Link')


    def click_registration_button(self):
        self.registration_button.click()

    def click_login_button(self):
        self.login_button.click()
        self.check_current_url(re.compile('.*/#/auth/login'))
