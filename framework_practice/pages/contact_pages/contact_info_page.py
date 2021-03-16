from framework_practice.pages.basepage import BasePage
from framework_practice.pages.contact_pages.contact_detail_page import ContactDetailPage


class ContactInfoPage(BasePage):
    def goto_contact_detail_page(self):
        # self.find_click('//*[@resource-id="com.tencent.wework:id/igo"]')
        self.parse_action('../pages/contact_pages/contact_info_page.yaml', 'goto_contact_detail_page')
        return ContactDetailPage(self.driver)