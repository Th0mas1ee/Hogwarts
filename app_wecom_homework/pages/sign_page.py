from app_wecom_homework.pages.basepage import BasePage


class SignPage(BasePage):
    def sign(self):
        # self.find_click("//*[@text='外出打卡']")
        # self.find_click("//*[contains(@text, '次外出')]")
        # self.find("//*[@text='外出打卡成功']")
        self.parse_action("../pages/sign_page.yaml", "sign")

    def first_sign(self):
        self.parse_action("../pages/sign_page.yaml", "first_sign")
