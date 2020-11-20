import pymysql

#连接数据库配置
host = '192.168.4.112'
port = 33307
database = 'speech'
username = 'speech'
password = '7DAM3jwxLnpvPDv68B3H4GPxgTSP24BA'
charset = 'utf8'
#pymysql.Connect时charset设置应该是utf8而不是utf-8 ！！！

class DB:
    def __init__(self):
        #建立数据库连接，设置 autocommit=True 自动提交事务
        self.coon = pymysql.connect(
            host = host,
            port = port,
            db = database,
            user = username,
            passwd = password,
            charset = charset,
            autocommit = True
        )
        #创建游标
        self.cur = self.coon.cursor()


    def __del__(self):# 析构函数，实例删除时触发 数据清除
        # 关闭游标
        self.cur.close()
        #关闭数据库
        self.coon.close()

    def query(self,table_name,field_name,value):
        #检查连接是否断开，如果断开就进行重连
        self.coon.ping(reconnect=True)
        # value需加单引号，否则报错
        sql = "select * from {} where {} = '{}'".format(table_name,field_name,value)
        # 使用execute执行sql
        self.cur.execute(sql)
        # 使用fetchall获取查询结果
        result = self.cur.fetchall()
        # self.conn.commit()
        return result

    def exec(self,sql):
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.coon.ping(reconnect=True)
            self.cur.execute(sql)
            self.coon.commit()
        except Exception as e:
            # 回滚所有更改
            self.coon.rollback()
            print(str(e))

    def check_user(self,table_name,field_name,value):
        result = self.query(table_name,field_name,value)
        return True if result else False

    def del_user(self,table_name,field_name,value):
        self.exec("delete from {} where {} = '{}'".format(table_name,field_name,value))

if __name__ == '__main__':
    db = DB()  # 实例化一个数据库操作对象
    project_number = '个人不带测试001'
    project_table = 'm_project'
    project_name = 'project_name'
    res = db.query(project_table,project_name,project_number)
    print(res)
    if res:
        print('返回成功')


