"""
读取Excel中的测试用例，使用unittest来进行断言
"""
import unittest
import paramunittest
import urllib.parse

from testFile.geturlParams import geturlParams
from testFile.readConfig import ReadConfig
from testFile.readExcel import readExcel
from common.configHttp import RunMain


readconfig = ReadConfig()
login_xls = readExcel().get_xls('userCase.xlsx','login')

class testTaskTypeInfo(unittest.TestCase):
    def setUp(self):
        """

               :return:
               """
        print('测试开始前的准备')

    def test_get_longvoice_list(self):



    def tearDown(self):
        """

               :return:
               """
        print('测试结束，输出log日志，完结\n\n')
