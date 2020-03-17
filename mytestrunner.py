# encoding=utf-8

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
