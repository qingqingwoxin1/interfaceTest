"""
工具类封装
"""
import hashlib
import base64
import time


class Utility:
    @staticmethod
    def md5(key):
        """
        md5加密算法
        :param key:
        :return:
        """
        value = hashlib.md5()
        value.update(key.encode())
        return value.hexdigest()

    @staticmethod
    def b64_encode(key):
        """
        b64加密
        :param key:
        :return:
        """
        value = base64.b64encode(key.encode())
        return value.decode()

    @staticmethod
    def md5_join_b64(key):
        """
        md5+b65得到完整加密字符串
        :param key:
        :return:
        """
        value = key + "MAGIC" #标啊标必须加上MAGIC进行加密
        md5 = Utility.md5(value)
        b64 = Utility.b64_encode(key)
        return md5 + b64

    @staticmethod
    def print_run_time(func):
        """
        脚本的运行时长
        :param func:
        :return:
        """
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print("脚本总运行时长为：%f" % (end - start))

        return wrapper


if __name__ == '__main__':

    # @Utility.print_run_time
    # def fun1():
    #     for i in range(100000):
    #         pass
    #
    #
    # fun1()
    res = Utility.md5_join_b64("1590000000")
    print(res)

