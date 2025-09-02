from playwright.sync_api import expect, Page
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-email-input').locator("input")
        self.username_input = page.get_by_test_id('registration-form-username-input').locator("input")
        self.pasword_input = page.get_by_test_id('registration-form-password-input').locator("input")
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_button = page.get_by_test_id('registration-page-login-link')

    def fill_registration_form(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.pasword_input.fill(password)
        expect(self.pasword_input).to_have_value(password)

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_button(self):
        self.login_button.click()

