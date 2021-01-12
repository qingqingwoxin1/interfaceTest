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
from common.util import Utility

readconfig = ReadConfig()
Info_xls = readExcel().get_xls('userCase.xlsx', 'Info')
util = Utility()


# 调用我们的geturlParams获取我们拼接的url
# url = geturlParams().get_url(readConfig.get_http('baseurl_first'),'')

@paramunittest.parametrized(*Info_xls)
class testInfo(unittest.TestCase):
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
        # 定义变量的值
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
        #获取测试名称
        self.case_name

    def setUp(self):
        """

        :return:
        """
        print('测试开始前的准备')

    def test_Info(self):
        self.checkResult()

    def checkResult(self):  # 断言
        url = geturlParams().get_url(readconfig.get_http('baseurl_first'),
                                     self.request_path)  # 调用我们的geturlParams获取我们拼接的url
        new_url = url + self.request_data
        data = dict(urllib.parse.parse_qsl(
            urllib.parse.urlsplit(
                new_url).query))  # 将一个完整的URL中的name=&password=转换为{'username':'xxx','password':'bbb'}
        #调用util进行加密
        # userid = util.md5_join_b64(data["userid"])
        #
        # #把加密后的值在替换到相应的位置
        # data["userid"] = userid
        info = RunMain().run_main(self.request_method, url, data,
                                  files=None)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = info.json()  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        if self.case_name == 'Info_success':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(self.expect_code, ss['code'])

        if self.case_name == 'Info_userid_error':  # 同上
            self.assertEqual(self.expect_code, ss['code'])

    def tearDown(self):
        """

        :return:
        """
        print('测试结束，输出log日志，完结\n\n')


if __name__ == '__main__':
    unittest.main(verbosity=2)
