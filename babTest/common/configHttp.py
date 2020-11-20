"""
这个文件主要来通过get、post、put、delete等方法进行http请求，并拿到请求响应
"""

import requests
import json
from testFile.readConfig import ReadConfig

readconfig = ReadConfig()


# headers = {'token:',ReadConfig().get_token('token')}
class RunMain():
    def send_post(self, url=None, data=None, files=None):
        # 封装post请求，参数按照顺序传入
        result = requests.post(url=url, data=data, files=files)  # 因为这里要封装post方法，所以这里的url和data值不能写死
        # res = json.dumps(result.json(), ensure_ascii=False, sort_keys=True,separators=(',',':'))
        return result

    def send_get(self, url=None, data=None):
        result = requests.get(url=url, params=data)
        # result = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def run_main(self, method, url, data,
                 files):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求,URL,DATA和files为空，不然报错
        res = None
        if method == 'post':
            res = self.send_post(url, data, files)
        elif method == 'get':
            res = self.send_get(url, data)
        else:
            print('method错误！！！')
        return res


if __name__ == '__main__':
    # data = ''
    # res = RunMain().run_main('pos','',data=data)
    run = RunMain()
    url = "http://test.speech.imagicdatatech.com/index.php/Api/Login/login?"
    data = {'user_name': '06f07c9872f28b7a8bae8ee00cd63b96MTU5MDAwMDAwMDA=',
            'user_pwd': 'f0edcf18976257492aadc5ea8c80a779MTIzNDU2', 'device_token': 'android'}
    res = run.send_post(url, data)
    print(res)
