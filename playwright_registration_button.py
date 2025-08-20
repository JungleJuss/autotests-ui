from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    button_registration = page.get_by_test_id('registration-page-registration-button')
    expect(button_registration).to_be_disabled()

    email_field = page.get_by_test_id('registration-form-email-input').locator('input')
    email_field.fill("user.name@gmail.com")

    user_field = page.get_by_test_id('registration-form-username-input').locator('input')
    user_field.fill("username")

    password_field = page.get_by_test_id('registration-form-password-input').locator('input')
    password_field.fill("password")

    expect(button_registration).to_be_enabled()

