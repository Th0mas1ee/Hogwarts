from framework_practice.pages.basepage import BasePage


class ManualAddMemberPage(BasePage):
    def add_member_manually(self, name, phone_number):
        # self.find_input('//*[@resource-id="com.tencent.wework:id/b7m"]', name)
        # self.find_input('//*[@resource-id="com.tencent.wework:id/fwi"]', phone_number)
        # self.find_click('//*[@resource-id="com.tencent.wework:id/aj_"]')
        self._params['name'] = name
        self._params['phone_number'] = phone_number
        self.parse_action('../pages/manual_add_member_page.yaml', 'add_member_manually')

    def verify_add_success(self):
        self.parse_action('../pages/manual_add_member_page.yaml', 'verify_add_success')