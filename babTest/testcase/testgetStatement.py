import selenium
import unittest
import urllib.parse
import paramunittest

from testFile.geturlParams import geturlParams
from testFile.readConfig import ReadConfig
from testFile.readExcel import readExcel
from common.configHttp import RunMain
from common.util import Utility

readconfig = ReadConfig()
getStatement_xls = readExcel().get_xls('userCase.xlsx', 'getStatement')
util = Utility()

@paramunittest.parametrized(*getStatement_xls)
class testGetStatement(unittest.TestCase):
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
        print("测试开始前准备")

    def test_into_statement(self):
        self.checkResult()

    def checkResult(self):
        url = geturlParams().get_url(readconfig.get_http('baseurl_first'),
                                     self.request_path)  # 调用我们的geturlParams获取我们拼接的url
        new_url = url + self.request_data
        data = dict(urllib.parse.parse_qsl(
            urllib.parse.urlsplit(
                new_url).query))  # 将一个完整的URL中的name=&password=转换为{'username':'xxx','password':'bbb'}
        # 调用util进行加密
        # username = util.md5_join_b64(data["user_name"])
        # user_pwd = util.md5_join_b64(data["user_pwd"])
        # # 把加密后的值在替换到相应的位置
        # data["user_name"] = username
        # data["user_pwd"] = user_pwd
        info = RunMain().run_main(self.request_method, url, data,
                                  files=None)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = info.json()  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        if self.case_name == 'getStatement_success':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(self.expect_code, ss['code'])
        if self.case_name == 'getStatement_error':  # 同上
            self.assertEqual(self.expect_code, ss['code'])

    def tearDown(self):
        """

        :return:
        """
        print("测试结束，输出log日志，完结\n\n")

if __name__ == '__main__':
    unittest.main(verbosity=2)
