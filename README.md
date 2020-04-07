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
  >
  > pip install ddt

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

  ### APP API自动化测试

  #### API

  > API (Application Programming Interface， 简称API)，又称为应用编程接口，就是软件系统不同组成部分衔接的约定。

  API种类：

  - 面向对象语言的API
  - 库与框架的API
  - API与协议
  - API与设备接口
  - Web API - 就是APP API测试中要测试的HTTP API

  ##### HTTP API

  HTTP中的8种不同方法：

  - **GET**：表示客户端需要请求服务器的某个资源，对应DB中的Select操作，为http请求常用方法 
  - **POST**： 一般用于向系统中更新数据，对应DB中的Update操作，为http请求常用方法；参数在Requet-Body中传递 ；相比较Get，较为安全
  - PUT：一般用于向系统中插入数据(当然，其功能Post也能实现，与Post有很多相似之处),对应DB中的Insert操作；传输内容放在Request-Body中；不安全，不带验证机制，故一般不使用该方法
  - DELETE：一般用于向系统中删除数据，对应DB中的Delete操作；不带验证机制，故不安全
  - OPTIONS： 一般用来询问URI支持的方法；查询服务器的性能
  - HEAD：用法与Get一样，只不过Head只返回Http-Responce头部信息；由于Head只返回头部信息(相对于Get，轻量级)，故一般被用于确认URI的有效性，资源更新的日期时间等
  - TRACE：追踪路径，如追踪一个资源请求中间所经过的代理；回显服务器收到的请求，主要用于测试或诊断
  - CONNECT：隧道协议连接代理


#### 抓包神奇Fiddler

##### 环境准备

- Fiddler安装 - [官网下载地址](https://www.telerik.com/download/fiddler)

- 基本设置

  打开Fiddler Tool->Fiddler Options->HTTPS 。 （配置完后记得要重启Fiddler）

  ![](G:\other\img\images\https_setting.png)

  选中"Decrpt HTTPS traffic",   Fiddler就可以截获HTTPS请求，第一次会弹出证书安装提示，若没有弹出提示，勾选Actions-> Trust Root Certificate，另外，如果你要监听的程序访问的 HTTPS 站点使用的是不可信的证书，则请接着把下面的 “Ignore servercertificate errors” 勾选上。

  ![](G:\other\img\images\trust_root_certificate.png)

##### 工作原理

![](G:\other\img\images\fiddler.png)

> 注意：Fiddler 是以代理web服务器的形式工作的，它使用代理地址:127.0.0.1，端口:8888。当Fiddler退出的时候它会自动注销，这样就不会影响别的 程序。不过如果Fiddler非正常退出，这时候因为Fiddler没有自动注销，会造成网页无法访问。解决的办法是重新启动下Fiddler。

##### 基本界面

![](G:\other\img\images\fiddler_userFace.png)

##### 设置断点修改Request/Response

- Rules - Automatic BreakPoints - Before Requests/After Requests（但是这样会拦截所有请求）

- 通过工具栏设置断点

  ![工具栏断点](G:\other\img\images\break_point.png)

  如图，箭头所指的位置时可以点击的。共三种状态：
  空白：不设置断点。
  箭头向上：表示断点请求。此时客户端的请求是无法直接到达目标服务器的，需要手动控制。
  箭头向下：表示断点响应。此时目标服务器的响应是无法直接到达客户端的，需要手动控制。

- 通过命令设置断点

  在上图框起来的上方的黑色区域就是命令行，在命令行中输入命令: 

  ```
  bpu www.baidu.com  （断点请求）
  bpu (清除拦截的请求断点)
  bpuafter www.baidu.com（断点响应）
  bpuafter (清除拦截的响应断点)
  这种方法只会中断指定的域名，如示例命令中的www.baidu.com
  ```

- **AutoResponder**标签 - Fiddler 的AutoResponder tab允许你从本地返回文件，而不用将http request 发送到服务器上。

##### 构造HTTP请求

Composer允许自定义请求发送到服务器，可以手动创建一个新的请求，也可以在会话表中，拖拽一个现有的请求。

Parsed模式下你只需要提供简单的URLS地址即可（如下图，也可以在RequestBody定制一些属性，如模拟浏览器User-Agent）。

![](G:\other\img\images\composer_get.png)

##### 抓取手机数据包

![](G:\other\img\images\mobile_fiddler_setting.png)

fiddler监听端口默认是 8888，你可以把它设置成任何你想要的端口。勾选上 “Allow remote computersto connect” ，允许远程设备连接。

为了减少干扰，可以去掉 “Act assystem proxy on startup” 。

###### 手机端(客户端)设置

- 首先查看电脑的 IP 地址，确保手机和电脑在同一个局域网内。（cmd命令行内输入ipconfig）

- 将 Fiddler 代理服务器的证书导到手机上才能抓这些 APP 的包。导入的过程:打开浏览器，在地址栏中输入代理服务器的 IP 和端口（即电脑的IP加fiddler的端口），会看到一个Fiddler 提供的页面，然后确定安装就好了

  ![](G:\other\img\images\download_cert.png)

- 打开 WiFi 设置页面，选择要连接的 wifi ，并且长按，在弹出的对话框中，选择“修改网络”。在接下来弹出的对话框中，勾选“显示高级选项”。在接下来显示的页面中，点击“代理”，选择“手动”。代理服务器主机名设为 PC 的 IP ，代理服务器端口设为 Fiddler 上配置的端口 8888，点”保存”。

#### 数据驱动DDT实现API接口自动化测试

- 安装requests模块

```
pip install requests
```

- 使用requests模块和ddt完成自动化api测试

  ```python
  import unittest
  import requests
  from ddt import ddt, data, unpack
  import sys
  
  reload(sys)
  sys.setdefaultencoding('utf-8')
  
  @ddt
  class HttpTestCase(unittest.TestCase):
      def setUp(self):
          print "开始"
  
      def tearDown(self):
          print "结束"
  
      @data('101010100', '101250101', '101250301', '101250603', '101251003')
      def testGet(self, city_id):
          # headers = {
          #     "User-Agent": "test"
          # }
          # cookies = {}
  
          result = requests.get("http://www.weather.com.cn/data/sk/" + city_id + ".html")
          result.encoding = 'utf-8'
          print result.text
  
          self.assertTrue(city_id in result.text)
  
  
  if __name__ == '__main__':
      unittest.main()
  
  ```

  > post和get类似，post请求会多一个params，也是一个字典，key和value的形式，调用requests.post(url, data=params, headers = headers, cookies = cookies)。

#### Android Native APP自动化(Python)

##### 自动化测试工具Appium

> **Appium** 是一个开源、跨平台的自动化测试工具，用于测试**Native（原生）**和**Hybrid（混合）**应用，支持iOS，Android和FirefoxOS平台。
>
> 在Android平台，是基于UIAutomator 框架。

###### Appium的理念

- 无需重新编译应用
- 不局限于语言和框架
- 无需重复造轮子，接口统一
- 无论精神上，还是名义上，必须开源（免费）

###### Appium的特点

- 跨架构，Native、Hybrid、Webview
- 跨设备，Android、iOS、Firefox OS
- 跨语言，Java、Python、Ruby、PHP、JavaScript
- 跨进程，不依赖源码（基于UIAutomator）

![Appium原理](G:\other\img\images\appium.jpg)

###### 脚本设计原则

**LOVE原则**

- L：Locate 定位元素
- O：Operate 操作元素
- V：Verify 验证结果
- E：Exception 处理异常

###### 自动化测试脚本demo编写

下面的demo是对系统自带的计算器APP进行测试的，界面元素的id和包名都是通过UIAutomator viewer获取的。

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

先运行Appium，点击android图标进行设置，主要设置platformVersion，我是用的Appium版本为appium1.4.16，由于appium1.4.16版本最高只支持安卓6.0版本，所以可以[参考这篇文章](https://www.jianshu.com/p/0136e26eee36)进行一些修改设置，然后运行Appium启动连接，再运行上面的demo，可以得到下面的输出结果：

```
Testing started at 11:56 ...
E:\Python27\python.exe "E:\Program Files\JetBrains\PyCharm Community Edition 2019.1.3\helpers\pycharm\_jb_unittest_runner.py" --target unittestdemo.MyTestCase
Launching unittests with arguments python -m unittest unittestdemo.MyTestCase in F:\code\AutomatedTestingDemo


Ran 1 test in 16.699s

OK

Process finished with exit code 0
```

###### Appium常用的相关API的介绍

- 控件定位

  | 方法                                 | 说明                                                         | 备注                                                         |
  | :----------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | find_element_by_id                   | 通过元素的id定位，返回含有该属性的元素，在UIAutomator viewer上即resource id | 找不到元素时会抛出异常，以下同理                             |
  | find_elements_by_id                  | 通过元素的id定位,返回含有该属性的所有元素                    | 找不到元素时不会抛出异常，以下同理                           |
  | find_element_by_name                 | 通过元素Name定位，返回含有该属性的元素，对于android，即text属性 |                                                              |
  | find_elements_by_name                | 通过元素Name定位（元素的名称属性text），含有该属性的所有元素 |                                                              |
  | find_element_by_xpath                | 通过Xpath定位，返回含有该属性的元素                          |                                                              |
  | find_elements_by_xpath               | 通过Xpath定位，返回含有该属性的所有元素                      |                                                              |
  | find_element_by_class_name           | 通过元素class name属性定位,返回包含该属性的元素              |                                                              |
  | find_elements_by_class_name          | 通过元素class name属性定位,返回包含该属性的所有元素          | 该字段存在的意义主要是为了一些有残障的人士准备的，方便他们使用程序 |
  | find_element_by_accessibility_id     | 通过accessibility id定位，在android app上相当于content-description字段，而在ios app 上accessibility identifier字段 | 同上                                                         |
  | find_elements_by_accessibility_id    | 同上                                                         |                                                              |
  | find_element_by_android_uiautomator  | 根据UIautomator定位元素                                      | 仅android                                                    |
  | find_elements_by_android_uiautomator | 同上                                                         | 仅android                                                    |
  | find_element_by_ios_uiautomation     | 在iOS中通过uiautomation找到一个元素                          | 仅iOS                                                        |
  | find_elements_by_ios_uiautomation    | 同上                                                         | 仅iOS                                                        |

- 动作操作（手势操作）

  | 方法                                                       | 说明                                                         | 备注                                                         |
  | ---------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | click                                                      | 点击                                                         | element.click()                                              |
  | send_keys                                                  | 在元素中模拟输入                                             | 开启appium自带的输入法并配置了appium输入法后，即unicodeKeyboard、resetKeyboard，可以输入中英文 |
  | clear                                                      | 清除输入的内容                                               | element.clear()                                              |
  | swipe(self, start_x, start_y, end_x, end_y, duration=None) | 滑动，主要用于缓慢滑动，从（start_x, start_y）点滑动到（end_x, end_y）点，可以自定义duration【毫秒】滑动时间 | driver.swipe(100,100,100,400)                                |
  | flick(self, start_x, start_y, end_x, end_y)                | 快速滑动                                                     | 主要用于快速滑动,无duration，如View切换，按住（start_x, start_y）点后快速滑动至（end_x, end_y）点 |
  | shake                                                      | 摇一摇                                                       |                                                              |
  | lock                                                       | 锁屏                                                         | iOS专有                                                      |
  | scroll(self, origin_el, destination_el)                    | 滚动                                                         | 从元素origin_el滚动至元素destination_el，只有iOS可以使用     |
  | drag_and_drop(self, origin_el, destination_el)             | 拖放                                                         | 将元素origin_el拖到目标元素destination_el                    |
  | zoom(self, element=None, percent=200, steps=50)            | 在元素上执行放大                                             | driver.zoom(element)#默认分成50步完成,放大量为200%           |
  | pinch(self, element=None, percent=200, steps=50)           | 在元素上执行缩小                                             | driver.pinch (element)                                       |
  | tap(self, positions, duration=None)                        | 模拟手指点击（最多五个手指），可设置按住时间长度（单位毫秒），positions参数为单位为元组的列表，如[(x1,y1),(x2,y2)] | driver.tap([(300,500)],10)                                   |
  | keyevent                                                   | 发送按键码（安卓仅有）                                       | KEYCODE_HOME (按键Home) : 3 ；KEYCODE_MENU (菜单键) : 82 ；KEYCODE_BACK (返回键) : 4` |

- 获取相关元素及设备相关信息

  | 方法             | 说明                                      | 备注                                    |
  | ---------------- | ----------------------------------------- | --------------------------------------- |
  | get_window_size  | 获取当前设备的宽、高                      | width=driver.get_window_size()['width'] |
  | location         | 获取元素的左上角坐标                      | x=element.location['x']                 |
  | size             | 获取元素的宽、高                          | width=element.size['width']             |
  | current_activity | 获取设备当前的activity                    | driver.current_activity                 |
  | context          | 获取当前会话的当前上下文                  | driver.context                          |
  | app_strings      | 对于Android，获取app的strings.xml文件内容 | ios待试                                 |

- 其他操作（系统操作如网络等、截图）

  | 方法                                                 | 说明                                      | 备注                                                         |
  | ---------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------ |
  | wait_activity（self, activity, timeout, interval=1） | 等待指定activity的出现，返回true or false | 默认是轮询间隔是1s，需要值得注意的是这里的参数是current_activity打印出来的值，即不包含包名 |
  | quit                                                 | 退出                                      | 退出脚本运行，并关闭每个相关的窗口连接                       |
  | background_app                                       | 后台运行                                  | 把app放置于后台运行，设置时间seconds，单位s，相当于一段时间后重启app，而不是home将app放置后台 |
  | save_screenshot(self, filename)                      | 截图                                      | filename参数为路径，包含文件名称                             |
  | is_app_installed                                     | 指定App是否安装                           | 参数为包名，已安装返回True，否则返回False                    |
  | remove_app                                           | 卸载指定app                               | 参数为包名                                                   |
  | install_appt(self, filename)                         | 安装指定app                               | filename参数为路径，包含apk名称                              |
  | launch_app                                           | 启动app                                   | 启动的app为desired_caps里设置的app                           |
  | close_app                                            | 关闭app                                   | 关闭的app为desired_caps里设置的app                           |
  | start_activity                                       | 启动指定activity                          | 参数为packageName和activityName                              |




#### Android Native APP自动化(Python)

针对于Hybrid的App，Appium是基于Selendroid框架实现，而Selendroid框架又是基于Instrumentation框架实现的。

> 可见，Appium本身是借助于其他框架控制APP。

##### Selendroid的架构

![selendroid原理](G:\other\img\images\selendroid.png)

##### 定位页面元素

- 原生页面元素：使用UIAutomator viewer定位

- hybrid页面原色： 使用Chrome浏览器的Inspector工具（打开浏览器，按F12进入开发者模式，先切换成手机显示模式，然后在定位到元素后，在其对应的代码里右键-copy XPath，其他浏览器也可以）。

  ![copy XPath](G:\other\img\images\copy_xpath.jpg)

##### 脚本设计原则

**S-LOVE原则（<API19）**

- S：Switch切换上下文
- O：Operate 操作元素
- V：Verify 验证结果
- E：Exception 处理异常

##### 基于Selendroid的自动化脚本实现

在页面里搜索一个关键词，并验证和预期一致

- Appium的配置、启动

  ![appium的设置](G:\other\img\images\appium_selendroid_set.jpg)

- 脚本的初始化

  ![appium启动成功](G:\other\img\images\appium_launch.jpg)

- 脚本的实现 - S-LOVE原则

  ```python
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
          input_url.send_keys("http://wap.sogou.com")
  
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
  ```

- 脚本的运行

  ```
  Testing started at 18:47 ...
  E:\Python27\python.exe "E:\Program Files\JetBrains\PyCharm Community Edition 2019.1.3\helpers\pycharm\_jb_unittest_runner.py" --target HybridScript.MyTestCase.testSearch
  Launching unittests with arguments python -m unittest HybridScript.MyTestCase.testSearch in F:\code\AutomatedTestingDemo\hybrid_app
  
  
  Ran 1 test in 39.463s
  
  OK
  
  Process finished with exit code 0
  [u'WEBVIEW_0', u'NATIVE_APP']
  WEBVIEW_0
  ```

  