from framework_practice.pages.basepage import BasePage
from framework_practice.pages.contact_pages.contact_edit_page import ContactEditPage


class ContactDetailPage(BasePage):
    def goto_contact_edit_page(self):
        # self.find_click('//*[@resource-id="com.tencent.wework:id/bct"]')
        self.parse_action('../pages/contact_pages/contact_detail_page.yaml', 'goto_contact_edit_page')
        return ContactEditPage(self.driver)