from app_wecom_homework.pages.basepage import BasePage
from app_wecom_homework.pages.contact_page import ContactPage
from app_wecom_homework.pages.workspace_page import WorkspacePage


class InformationPage(BasePage):
    def goto_workspace_page(self):
        self.parse_action('../pages/information.yaml', "goto_workspace_page")
        return WorkspacePage(self.driver)

    def goto_contact_page(self):
        self.parse_action('../pages/information.yaml', "goto_contact_page")
        return ContactPage(self.driver)