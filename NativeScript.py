# encoding=utf-8


import unittest
from appium import webdriver
from ddt import ddt, data, unpack


@ddt
class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '9.0', 'deviceName': '192.168.115.101:5555',
                        'appPackage': 'com.android.calculator2', 'appActivity': '.Calculator',
                        "unicodeKeyboard": "True", "resetKeyboard": "True"}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @data("30,352", "35,023", "12,345", "32,053")
    def test_something(self, expected_result):
        self.driver.find_element_by_id("digit_1").click()
        self.driver.find_element_by_id("digit_3").click()
        self.driver.find_element_by_id("digit_5").click()
        self.driver.find_element_by_id("op_add").click()
        self.driver.find_element_by_id("digit_8").click()
        self.driver.find_element_by_id("digit_9").click()
        self.driver.find_element_by_id("op_mul").click()
        self.driver.find_element_by_id("digit_3").click()
        self.driver.find_element_by_id("digit_9").click()
        self.driver.find_element_by_id("digit_2").click()
        self.driver.find_element_by_id("eq").click()

        result = self.driver.find_element_by_id("result").text
        self.assertEqual(result, expected_result)

    def tearDown(self):
        # 一定记得退出driver，不然下次运行会直接报错，除非在Appium中手动停止连接
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
