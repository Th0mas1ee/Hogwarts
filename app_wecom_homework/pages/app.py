from appium import webdriver

from app_wecom_homework.pages.information_page import InformationPage


class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "WeCom"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        # caps["dontStopAppOnReset"] = "true"
        # caps["skipDeviceInitialization"] = "true"
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return InformationPage(self.driver)