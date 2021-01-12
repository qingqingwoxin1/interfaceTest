
"""
自己写的提供本地测试的接口服务
通过flask搭建web服务器
"""
import flask
from flask import request
import json

# 创建flask对象
server = flask.Flask(__name__)


# 定义路由，登录接口的路径和方法
@server.route('/login', methods=['get', 'post'])
def login():
    username = request.values.get('username')
    password = request.values.get('password')
    if username and password:
        if username == 'liuguiju' and password == '123456':
            resu = {
                'code': 200,
                'message': '登录成功'
            }
            return json.dumps(resu, ensure_ascii=False)
        else:
            resu = {
                'code': -1,
                'message': '账户密码错误'
            }
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {
            'code': 10001,
            'message': '参数不能为空！'
        }
        return json.dumps(resu, ensure_ascii=False)


@server.route('/', methods=['get', 'post'])
def index():
    return json.dumps({"code": 200, "msg": "访问首页成功！"})


@server.route('/about', methods=['get', 'post'])
def about():
    return json.dumps({"code": 200, "msg": "访问关于页面成功！"})


@server.route('/demo', methods=['get', 'post'])
def demo():
    return json.dumps({"code": 200, "msg": "访问demo成功！"})


if __name__ == '__main__':
    server.run(debug=True, port=8888, host='127.0.0.1')