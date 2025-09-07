from components.base_component import BaseComponent
from playwright.sync_api import Page
import re

from components.sidebar_list_item_component import SidebarListItem


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItem(page, 'logout')
        self.courses_list_item = SidebarListItem(page, 'courses')
        self.dashboard_list_item = SidebarListItem(page, 'dashboard')

     def check_visible(self):
         self.logout_list_item.check_visible("Logout")
         self.courses_list_item.check_visible("Courses")
         self.dashboard_list_item.check_visible("Dashboard")

    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))
