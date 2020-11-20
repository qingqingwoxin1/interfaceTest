"""
获取接口的URL、参数、method等
"""

from testFile.readConfig import *

readconfig = ReadConfig()

class geturlParams(): # 定义一个方法，将从配置文件中读取的进行拼接
    def get_url(self,baseurl,path):
        new_url = readconfig.get_http('scheme') + '://' + baseurl + '/' + path + '?'
        # logger.info('new_url'+new_url)
        return new_url

if __name__ == '__main__':  # 验证拼接后的正确性
    print(geturlParams().get_url(readconfig.get_http('baseurl_first'), 'api/public/ucenter/project'))