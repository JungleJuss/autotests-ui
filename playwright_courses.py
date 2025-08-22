from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_field = page.get_by_test_id('registration-form-email-input').locator('input')
    email_field.fill("user.name@gmail.com")

    user_field = page.get_by_test_id('registration-form-username-input').locator('input')
    user_field.fill("username")

    password_field = page.get_by_test_id('registration-form-password-input').locator('input')
    password_field.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="browser-state-course.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state-course.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    title_courses = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(title_courses).to_be_visible()
    expect(title_courses).to_have_text("Courses")

    icon_courses = page.get_by_test_id("courses-list-empty-view-icon")
    expect(icon_courses).to_be_visible()

    noresult_text = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(noresult_text).to_be_visible()
    expect(noresult_text).to_have_text("There is no results")

    results_text = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(results_text).to_be_visible()
    expect(results_text).to_have_text("Results from the load test pipeline will be displayed here")

