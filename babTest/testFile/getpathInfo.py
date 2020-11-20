"""
获取项目绝对路径
"""

import os

# 获取getpathInfo文件的绝对路径
def get_path(file):
    path = os.path.split(os.path.realpath(file))[0] #[0]是去除路径的括号和引号，方便调用
    return path

if __name__ == '__main__':
    print("测试路径是否OK，路径为：",get_path('sql/uc_project'))


