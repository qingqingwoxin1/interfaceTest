"""
读取Excel中的测试用例，使用unittest来进行断言
"""
import unittest
import paramunittest
import urllib.parse
import time

# 导入相应的方法
from testFile.geturlParams import geturlParams
from testFile.readConfig import ReadConfig
from testFile.readExcel import readExcel
from common.configHttp import RunMain
from common.util import Utility
from common.configDB import DB

# 实例化参数
readconfig = ReadConfig()
addProjectAudit_xls = readExcel().get_xls('userCase.xlsx', 'addProjectAudit')
util = Utility()
db = DB()


@paramunittest.parametrized(*addProjectAudit_xls)
class addProjectAudit(unittest.TestCase):
    # 实例化Excel表中的数据
    def setParameters(self, case_no, case_name, path, parameter, method, expect_result, expect_content):
        """
               :param case_no:
               :param case_name:
               :param parameter:
               :param method:
               :param expect_result:
               :param path:
               :param expect_content:
               :return:
               """
        self.case_no = str(case_no)
        self.case_name = str(case_name)
        self.request_path = str(path)
        self.request_data = str(parameter)
        self.request_method = str(method)
        self.expect_code = int(expect_result)
        self.expect_content = str(expect_content)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """
        :return:
        """
        print('测试开始前的准备')

    def test_add_project_audit(self):
        self.chechResult()

    def chechResult(self):
        url = geturlParams().get_url(readconfig.get_http('baseurl_first'),
                                     self.request_path)  # 调用我们的geturlParams获取我们拼接的url
        new_url = url + self.request_data
        data = dict(urllib.parse.parse_qsl(
            urllib.parse.urlsplit(
                new_url).query))  # 将一个完整的URL中的name=&password=转换为{'username':'xxx','password':'bbb'}
        info = RunMain().run_main(self.request_method,url,data)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = info.json()  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        if self.case_name == 'addProjectAudit_success':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(self.expect_code, ss['code'])
        if self.case_name == 'addProjectAudit_error':  # 同上
            self.assertEqual(self.expect_code, ss['code'])

    def tearDown(self):
        """

        :return:
        """
        print('测试结束，输出log')


if __name__ == '__main__':
    unittest.main(verbosity=2)
