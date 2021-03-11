from time import sleep

import pytest
import yaml

from app_wecom_homework.pages.app import App


class TestSign:
    def setup(self):
        self.app = App()

    def tear_down(self):
        self.app.goto_main().find_click('//*[@text="消息"]')

    @pytest.mark.parametrize(("name", "phone_number"), yaml.safe_load(open('./add_contact_data.yaml')))
    def test_add_contact(self, name, phone_number):
        contact_page = self.app.goto_main().goto_contact_page()
        add_member_page = contact_page.goto_add_member_page()
        manual_add_member_page = add_member_page.goto_manual_add_member_page()
        manual_add_member_page.add_member_manually(name, phone_number)
        sleep(1)
        add_member_page.goto_contact_page()
        sleep(2)
        names = contact_page.get_contact_names()
        print(f'names: {names}')
        assert name in names