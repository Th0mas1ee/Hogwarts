from selenium.webdriver.common.by import By
from web_wecom_po.pages.base_page import BasePage
# 注册页面


class RegisterPage(BasePage):
    # 注册公司
    def register(self):
        # 输入公司名
        self.find(By.ID, 'corp_name').send_keys('Hello')
        # 输入公司所有人名称
        self.find(By.ID, 'manager_name').send_keys('Manager')
        return True
