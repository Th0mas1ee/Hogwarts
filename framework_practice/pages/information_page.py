from framework_practice.pages.basepage import BasePage
from framework_practice.pages.contact_pages.contact_page import ContactPage
from framework_practice.pages.workspace_page import WorkspacePage


class InformationPage(BasePage):
    def goto_workspace_page(self):
        self.parse_action('../pages/information.yaml', "goto_workspace_page")
        return WorkspacePage(self.driver)

    def goto_contact_page(self):
        self.parse_action('../pages/information.yaml', "goto_contact_page")
        return ContactPage(self.driver)