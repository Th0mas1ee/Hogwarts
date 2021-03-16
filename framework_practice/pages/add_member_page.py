from framework_practice.pages.basepage import BasePage
from framework_practice.pages.manual_add_member_page import ManualAddMemberPage


class AddMemberPage(BasePage):
    def goto_manual_add_member_page(self):
        self.parse_action('../pages/add_member_page.yaml', 'goto_manual_add_member_page')
        return ManualAddMemberPage(self.driver)

    def goto_contact_page(self):
        self.parse_action('../pages/add_member_page.yaml', 'goto_contact_page')