from framework_practice.pages.basepage import BasePage


class ContactEditPage(BasePage):
    def delete_contact(self):
        # self.find_click('//*[@resource-id="com.tencent.wework:id/esd"]')
        # self.find_click('//*[@resource-id="com.tencent.wework:id/bpc"]')
        self.parse_action('../pages/contact_pages/contact_edit_page.yaml', 'delete_contact')