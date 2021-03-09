from time import sleep

from web_wecom_po.pages.home_page import HomePage
# 注册的测试用例，前置条件为未登录企业微信


class TestRegister:
    def setup(self):
        self.homepage = HomePage()

    def test_register(self):
        """
        1. 从首页跳转到登陆页面；
        2. 从登陆页面跳转到注册页面；
        3. 注册公司；
        """
        assert self.homepage.goto_login().goto_register().register()
        sleep(3)