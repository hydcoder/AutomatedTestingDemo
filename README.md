# AutomatedTestingDemo
 自动化测试框架测试Demo

### Android APP 自动化测试

#### 自动化测试环境安装

- Node.js - [下载地址]( https://nodejs.org/en/download/)

- Android SDK - [官网](https://developer.android.com/)，[中文社区](http://tools.android-studio.org/index.php/sdk)

- UIAutomator - Android SDK下的一个工具

- Python - [下载地址](https://www.python.org/downloads/)

- Appium - [下载地址](https://bitbucket.org/appium/appium.app/downloads/)

- Appium-Python-Client - [下载地址](https://pypi.python.org/pypi/Appium-Python-Client/)，安装了Python后，也可以使用pip命令安装

- PyCharm - []下载地址(https://www.jetbrains.com/pycharm/download/)

  > 软件安装以及环境配置可以参考这篇文章：[参考文章](https://blog.csdn.net/zh175578809/article/details/76780054)

#### 编写自动化测试Demo

下面的demo是对系统自带的计算器APP进行测试的，界面元素的id和包名都是通过UIAutomator获取的。

```python
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
```

先运行Appium，点击android图标进行设置，主要设置platformVersion，我是用的Appium版本为appium1.4.16，由于appium1.4.16版本最高只支持安卓6.0版本，所以可以[参考这篇文章](https://www.jianshu.com/p/0136e26eee36)进行一些修改设置，然后运行Appium启动连接，再运行上面的demo，可以得到下面的输出结果：

```
E:\Python27\python.exe F:/code/AutomatedTestingDemo/test_demo/test_demo.py
35,023

Process finished with exit code 0
```

### Android APP 自动化测试框架

#### Unittest框架

> 使用unittest编写用例，必须遵守以下规则:
>
> 1、测试文件必须先import unittest；
>
> 2、测试类必须继承unittest.TestCase；
>
> 3、测试方法必须以“test_”开头；
>
> 4、测试类必须要有unittest.main()方法。

##### Test Fixture

> A test fixture represents the preparation needed to perform one or more tests, and any assoicate cleanup actions.

- setUp() : 进行测试前的初始化工作。
- testCase() : 进行测试工作，可以有很多个
- tearDown() : 执行测试后的清除工作。

使用unittest改写上面的自动化测试脚本

```python
import unittest
from appium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9.0'
        desired_caps['deviceName'] = '192.168.115.101:5555'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = '.Calculator'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_something(self):
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
        self.assertEqual(result, "35,023")

    def tearDown(self):
        # 一定记得退出driver，不然下次运行会直接报错，除非在Appium中手动停止连接
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
```

运行结果：

```
Testing started at 11:56 ...
E:\Python27\python.exe "E:\Program Files\JetBrains\PyCharm Community Edition 2019.1.3\helpers\pycharm\_jb_unittest_runner.py" --target unittestdemo.MyTestCase
Launching unittests with arguments python -m unittest unittestdemo.MyTestCase in F:\code\AutomatedTestingDemo


Ran 1 test in 16.699s

OK

Process finished with exit code 0
```

##### Test Case & Test Suite &Test Runner

官网的含义介绍：

> A test case is the smallest unit of testing. It checks for a specific response to a particular set of inputs. 测试用例是最小的测试单元。它检查对特定输入集的特定响应。
>
> A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests taht should be executed together. 测试套件是测试用例、测试套件或两者的集合。它用于聚合应该一起执行的测试。
>
> A test runner is a component thich orchestrates the execution of tests and provides the outcome to the user. 测试运行器是一个组件，它协调测试的执行并向用户提供结果。

###### 应用Test Suite 和Test Runner 运行自动化脚本

```python
import unittestdemo
import unittest


# 以一个类的维度去执行
cases = unittest.TestLoader.loadTestsFromTestCase(unittestdemo.MyTestCase)
# 可以一次添加多个cases
my_suite = unittest.TestSuite([cases])

# 添加单个测试用例，在使用ddt后，将会不可用
# my_suite = unittest.TestSuite()
# my_suite.addTest(unittestdemo.MyTestCase("test_something"))

my_runner = unittest.TextTestRunner(verbosity=2)
my_runner.run(my_suite)
```

##### 数据驱动DDT

[官网](https://pypi.org/project/ddt/)

> DDT(Data-Driven Tests) allows you to multiply one test case by runing it with different test data, and make it appear as multiple test cases.
>
> DDT（数据驱动测试）允许您将一个测试用例与不同的测试数据一起运行，从而使它显示为多个测试用例。

###### 数据驱动DDT的使用

- 准备第三方库

  > 首先安装ddt库， 其次在脚本中引入ddt

- 使用

  ```python
  import unittest
  from ddt import ddt, data, unpack
  
  # 声明该测试类采用ddt
  @ddt
  class MyTestCase(unittest.TestCase):
  
      # 使用元祖存放被测试的数据，一次只有一个参数的情况，每一组数据都会执行一次测试用例
      @data(1, 2, 3)
      def test_something(self, value):
          print value
          self.assertEqual(value, 2)
  
      # 使用元祖存放被测试的数据，一次有多个参数的情况，每一组数据都会执行一次测试用例
      @data((1, 2), (2, 3))
      @unpack
      def test_something(self, value1, value2):
          print value1, value2
          self.assertEqual(value2, value1 + 1)    
  
  if __name__ == '__main__':
      unittest.main()
      
  ```

- 用ddt改写测试系统计算器的测试脚本

  ```python
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
  
  ```

  