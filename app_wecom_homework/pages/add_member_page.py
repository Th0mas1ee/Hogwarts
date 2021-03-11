from app_wecom_homework.pages.basepage import BasePage
from app_wecom_homework.pages.manual_add_member_page import ManualAddMemberPage


class AddMemberPage(BasePage):
    def goto_manual_add_member_page(self):
        self.parse_action('../pages/add_member_page.yaml', 'goto_manual_add_member_page')
        return ManualAddMemberPage(self.driver)

    def goto_contact_page(self):
        self.parse_action('../pages/add_member_page.yaml', 'goto_contact_page')