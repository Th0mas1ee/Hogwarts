from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 使用cookie登录企业微信，完成导入联系人，加上断言验证


class TestWeb:
    def setup(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        # get_cookies() 获取当前页面的cookies
        # cookies = self.driver.get_cookies()
        # print(cookies)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851052855853'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'RKzorIdBwpXe_BU4tm5jJHau9YioFP79ol6Dz1hpm_8rzd6X6hO04Navcwii0l5x6A8ksgU67Q3ybHUTu42oDuKL99R6sLG9OeOt5Sa29JhUN8HbSw_8430cMip0tPBDoE_gAf2whgcrgPkqORZuzEMyhFpPGWZ4uhlrKL6Hm85NimRzUhoLhOgizxurdLyv-StqmuFTCNAhdexkXqiVV8vJ-6lM_oRxVNFq0huoY-on-lG0YbnLJIy38qdqc3IfGSP4o9jy0Vis8HVt-bB0zg'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851052855853'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325120426443'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '9zSaMDi8FB168x5wIxbaIKmHcGWzUCKSorqMbewrbqQVwQy_l3Nv6WqznNNAqJKn'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8122027'}, {'domain': '.qq.com', 'expiry': 1615217789, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'work.weixin.qq.com', 'expiry': 1615247578, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '50l464d'}, {'domain': '.qq.com', 'expiry': 1615304142, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1777273587.1615216043'}, {'domain': '.qq.com', 'expiry': 1678289742, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.351632617.1614333829'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645869827, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1617809745, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1646753729, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614333829,1615216043,1615217729'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '4349044402'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'c5fc6b1cb16e3439fa05a7746f107f2028cd0a71ea2d92c304444062ba9dd99f'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1615217729'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '40163385452129955'}, {'domain': '.qq.com', 'expiry': 1928661859, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '86f05d3feafb105d'}, {'domain': '.qq.com', 'expiry': 2147483645, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'PFzdz4hOfs'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys("D:\\Study\Hogwarts\\web_wecom_auto_login\\contact.xlsx")
        actual_text = self.driver.find_element(By.ID, "upload_file_name").text
        assert "contact.xlsx" == actual_text
