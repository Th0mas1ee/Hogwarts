from selenium.webdriver.common.by import By
from web_wecom_po.pages.base_page import BasePage
from web_wecom_po.pages.register_page import RegisterPage
# 登陆页面


class LoginPage(BasePage):
    # 跳转到注册页面
    def goto_register(self):
        # 点击注册按钮
        self.find(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return RegisterPage(self.driver)
