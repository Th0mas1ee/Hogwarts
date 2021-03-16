from time import sleep

from framework_practice.pages.basepage import BasePage
from framework_practice.pages.sign_page import SignPage


class WorkspacePage(BasePage):
    def goto_sign_page(self):
        # self.swip_click("打卡")
        self.parse_action("../pages/workspace_page.yaml", "goto_sign_page")
        sleep(2)
        return SignPage(self.driver)

