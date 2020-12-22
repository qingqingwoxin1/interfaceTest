import os
import configparser
from testFile.getpathInfo import *  # 引入我们自己的写的获取路径的类

path = get_path(__file__)  # 调用实例化，还记得这个类返回的路径为 D:\interfaceTest\testFile
config_path = os.path.join(path,
                           'config.ini')  # 这句话是在path路径下再加一级，最后变成 D:\interfaceTest\testFile\config.ini
config = configparser.ConfigParser()   # 调用外部的读取配置文件的方法
config.read(config_path,encoding='utf-8')


class ReadConfig():
    def get_http(self,name):
        value = config.get('HTTP',name)
        return value

    def get_email(self,name):
        value = config.get('EMAIL',name)
        return value

    def get_mysql(self,name):
        value = config.get('DATABASE',name)
        return value

    def get_version(self,name):
        value = config.get('VERSION',name)
        return value

    def get_system(self,name):
        value = config.get('SYSTEM',name)
        return value

    def get_cookie(self,name):
        value = config.get('COOKIE',name)
        return value

    def get_token(self,name):
        value = config.get('TOKEN',name)
        return value

    def get_userid(self,name):
        value = config.get('USERID',name)
        return value

    def get_MongoDB(self,name):
        value = config.get('MONGODB',name)
        return value

if __name__ == '__main__':
    print('mongodb host的值为：',ReadConfig().get_MongoDB("host"))