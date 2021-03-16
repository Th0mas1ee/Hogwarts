from framework_practice.contest import root_log
from framework_practice.pages.basepage import BasePage
from framework_practice.pages.contact_pages.contact_info_page import ContactInfoPage


class SearchContactPage(BasePage):
    def search_contact(self, contact_name):
        # self.find_input("//*[@resource-id='com.tencent.wework:id/gy9']", contact_name)
        self._params['contact_name'] = contact_name
        self.parse_action('../pages/contact_pages/search_contact_page.yaml', 'search_contact')

    def get_matched_contact_num(self):
        eles = self.parse_action('../pages/contact_pages/search_contact_page.yaml', 'get_matched_contact_num')
        if len(eles) == 0:
            num = 0
        else:
            num = len(eles) - 1
        root_log.info(f'Found {num} matched contacts.')
        return num

    def goto_first_contact_page(self):
        # self.find_click('//*[@resource-id="com.tencent.wework:id/gzp"]/android.widget.RelativeLayout[2]')
        self.parse_action('../pages/contact_pages/search_contact_page.yaml', 'goto_first_contact_page')
        return ContactInfoPage(self.driver)