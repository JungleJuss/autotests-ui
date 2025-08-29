from playwright.sync_api import expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        title_courses = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
        expect(title_courses).to_be_visible()
        expect(title_courses).to_have_text("Courses")

        icon_courses = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
        expect(icon_courses).to_be_visible()

        noresult_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
        expect(noresult_text).to_be_visible()
        expect(noresult_text).to_have_text("There is no results")

        results_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
        expect(results_text).to_be_visible()
        expect(results_text).to_have_text("Results from the load test pipeline will be displayed here")