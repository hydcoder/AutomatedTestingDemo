# encoding=utf-8

import unittest
import time
from appium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # 定义初始化的属性信息
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '6.0'
        self.desired_caps['deviceName'] = '192.168.115.101:5555'
        self.desired_caps['appPackage'] = 'com.hyd.miniwebbrowser'
        self.desired_caps['appActivity'] = '.MainActivity'
        self.desired_caps["unicodeKeyboard"] = "True"
        self.desired_caps["resetKeyboard"] = "True"
        self.desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    def testSearch(self):
        # Locate 定位输入框
        input_url = self.driver.find_element_by_id("et_url")
        # Operate 操作
        input_url.send_keys("https://wap.sogou.com")

        btn_search = self.driver.find_element_by_id("btn_search")
        btn_search.click()

        time.sleep(5)

        # Switch 切换当前的上下文
        print self.driver.contexts
        self.driver.switch_to.context('WEBVIEW_0')
        print self.driver.current_context
        time.sleep(5)

        # 定位web输入框
        web_input = self.driver.find_element_by_xpath('//*[@id="keyword"]')
        web_input.click()
        web_input.send_keys("2020")
        web_search_button = self.driver.find_element_by_xpath('//*[@id="searchform"]/div/div/div[1]/div[2]/input')
        web_search_button.click()
        time.sleep(5)

        # 检验查询结果
        first_result = self.driver.find_element_by_xpath('//*[@id="sogou_vr_30010212_1"]/div/div[1]/a[1]')
        self.assertTrue("2020" in first_result.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
