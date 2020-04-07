# coding=utf-8

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

