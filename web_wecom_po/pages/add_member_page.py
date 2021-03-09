from selenium.webdriver.common.by import By
from web_wecom_po.pages.base_page import BasePage

# 添加成员页面


class AddMemberPage(BasePage):
    # 添加成员
    def add_member(self, username, account, phone_number):
        # 输入用户名
        self.find(By.ID, 'username').send_keys(username)
        # 输入帐号
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        # 输入手机号码
        self.find(By.ID, 'memberAdd_phone').send_keys(phone_number)
        # 点击保存
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return True

    def get_member(self):
        locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")
        # 显示等待表头左侧复选框可点击
        self.wait_for_click(10, locator)
        # 获取姓名列的所有元素
        eles_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        names = []
        for ele in eles_list:
            names.append(ele.get_attribute("title"))    # 循环获取各个元素的title属性
        return names
