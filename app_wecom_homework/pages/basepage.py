from typing import List, Dict

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _params = {}

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element_by_xpath(locator)

    def finds(self, locator):
        return self.driver.find_elements_by_xpath(locator)

    def find_click(self, locator):
        self.find(locator).click()

    def find_input(self, locator, value):
        self.find(locator).send_keys(value)

    def swip_click(self, text):
        ele = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                       'new UiScrollable(new UiSelector().'
                                       'scrollable(true).instance(0)).'
                                       'scrollIntoView(new UiSelector().'
                                       f'text("{text}").instance(0));')
        ele.click()
        ele.click()

    def parse_action(self, path, func_name):
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            # print(f'function: {function}')
            steps: List[Dict] = function[func_name]
            # print(f'steps: {steps}')
        for step in steps:
            if step['action'] == 'find_click':
                self.find_click(step['locator'])
            elif step['action'] == 'find':
                self.find(step['locator'])
            elif step['action'] == 'finds':
                return self.finds(step['locator'])
            elif step['action'] == 'swip_click':
                self.swip_click(step['locator'])
            elif step['action'] == 'find_input':
                content: str = step['value']
                for param in self._params:
                    content = content.replace("{%s}"%param, self._params[param])
                self.find_input(step['locator'], content)