# Homepage
from selenium.webdriver.common.by import By
from web_wecom_po.pages.add_member_page import AddMemberPage
from web_wecom_po.pages.base_page import BasePage
from web_wecom_po.pages.login_page import LoginPage
from web_wecom_po.pages.register_page import RegisterPage


class HomePage(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    # 跳转到登录页面，前置条件为未登录企业微信
    def goto_login(self):
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return LoginPage(self.driver)

    # 跳转到注册页面，前置条件为未登录企业微信
    def goto_register(self):
        self.find(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn')
        return RegisterPage(self.driver)

    # 跳转到添加成员页面，前置条件为已登录企业微信
    def goto_add_member_page(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMemberPage(self.driver)
