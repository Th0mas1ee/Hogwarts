from time import sleep

import pytest
import yaml

from framework_practice.contest import root_log
from framework_practice.pages.app import App


class TestContact:
    def setup(self):
        self.app = App()

    # def tear_down(self):
    #     self.app.goto_main().find_click('//*[@text="消息"]')

    @pytest.mark.parametrize(("name", "phone_number"), yaml.safe_load(open('./add_contact_data.yaml')))
    def test_add_contact(self, name, phone_number):
        contact_page = self.app.goto_main().goto_contact_page()
        add_member_page = contact_page.goto_add_member_page()
        manual_add_member_page = add_member_page.goto_manual_add_member_page()
        manual_add_member_page.add_member_manually(name, phone_number)
        manual_add_member_page.verify_add_success()
        sleep(1)
        add_member_page.goto_contact_page()
        sleep(2)
        names = contact_page.get_contact_names()
        print(f'names: {names}')
        assert name in names

    @pytest.mark.parametrize('contact_name', ['111', '11111', '222'])
    def test_delete_contact(self, contact_name):
        search_contact_page = self.app.goto_main().goto_contact_page().goto_search_contact_page()
        search_contact_page.search_contact(contact_name)
        sleep(1)
        matched_num = search_contact_page.get_matched_contact_num()
        if matched_num == 0:
            err_msg = f"Couldn't find target contact, please check your input content."
            root_log.error(err_msg)
            raise err_msg
        search_contact_page.goto_first_contact_page().goto_contact_detail_page().goto_contact_edit_page().delete_contact()
        sleep(3)
        post_num = search_contact_page.get_matched_contact_num()
        assert (post_num == (matched_num - 1))