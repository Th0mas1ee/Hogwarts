import pytest
import yaml
from selenium.webdriver.common.by import By

from web_wecom_po.pages.home_page import HomePage
# 完成添加联系人PO封装，前置条件为已登录企业微信


class TestContact:
    def setup(self):
        self.homepage = HomePage()
        pass

    def teardown(self):
        # 由于复用浏览器，测试用例结束后需回到主页
        self.homepage.find(By.ID, "menu_index").click()

    # 实现参数化关联，并使用yaml文件驱动
    @pytest.mark.parametrize(("username", "account", "phone_number"), yaml.safe_load(open('./contact_data.yml')))
    def test_add_member(self, username, account, phone_number):
        # 从主页跳转到添加成员页面
        page = self.homepage.goto_add_member_page()
        # 添加一个成员
        page.add_member(username, account, phone_number)
        # 获取成员的姓名列表
        names = page.get_member()
        # print(f'username: {username}; type: {type(username)}')
        # 断言判断成员是否添加成功
        assert username in names
