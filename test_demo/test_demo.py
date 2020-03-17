# encoding=utf-8

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.0'
desired_caps['deviceName'] = '192.168.115.101:5555'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("digit_1").click()
driver.find_element_by_id("digit_3").click()
driver.find_element_by_id("digit_5").click()
driver.find_element_by_id("op_add").click()
driver.find_element_by_id("digit_8").click()
driver.find_element_by_id("digit_9").click()
driver.find_element_by_id("op_mul").click()
driver.find_element_by_id("digit_3").click()
driver.find_element_by_id("digit_9").click()
driver.find_element_by_id("digit_2").click()
driver.find_element_by_id("eq").click()

result = driver.find_element_by_id("result").text

if result == "30,352":
    print "pass"
else:
    print "fail"

# 一定记得退出driver，不然下次运行会直接报错，除非在Appium中手动停止连接
driver.quit()
