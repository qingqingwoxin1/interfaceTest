import smtplib                               #发送邮件模块
from email.mime.text import MIMEText            #定义邮件内容
from email.mime.multipart import MIMEMultipart  #用于传送附件
from testFile import readConfig
import os

read_conf = readConfig.ReadConfig()

#发送邮箱服务器
stmpserver =read_conf.get_email('stmpserver')

#发送邮箱用户名密码
user=read_conf.get_email('my_sender')
password=read_conf.get_email('my_pass')

#发送和接收邮箱
sender=read_conf.get_email('my_sender')
receives=[read_conf.get_email('addressee')]
path='../../babTest'
mail_path = os.path.join(path, 'result', 'report.html')  # 获取测试报告路径
def send_email():
    ret = True
    try:
        #发送邮件主题和内容
        subject=read_conf.get_email('subject')
        # content为邮件内容，一般发送的是报告里的内容，而报告文件一般会先生成伪Html格式的文件保存；
        content='<html><h1 style="color:red">请查收，谢谢!</h1></html>'
        #构造附件内容：定义附件，构造附件内容
        send_file=open(mail_path,'r',encoding='utf8').read()     #'rb'表示r读取，b表示二进制方式读取
        att=MIMEText(send_file,'base64','utf-8')                     #调用传送附件模块，传送附件
        att["Content-Type"]='application/octet-stream'
        att["Content-Disposition"]='attachment;filename="report.html"'  #附件描述外层要用单引号

        #构建发送与接收信息
        msgRoot=MIMEMultipart()                             #发送附件的方法定义为一个变量
        msgRoot.attach(MIMEText(content, 'html', 'utf-8'))  #发送附件的方法中嵌套发送正文的方法
        msgRoot['subject']=subject
        msgRoot['From']=sender
        msgRoot['To'] = ','.join(receives)
        msgRoot.attach(att)                                 #添加附件到正文中

        #SSL协议端口号要使用465
        smtp = smtplib.SMTP_SSL(stmpserver, 465)

        #HELO 向服务器标识用户身份
        smtp.helo(stmpserver)
        #服务器返回结果确认
        smtp.ehlo(stmpserver)
        #登录邮箱服务器用户名和密码
        smtp.login(user,password)

        # print("Start send email...")

        smtp.sendmail(sender,receives,msgRoot.as_string())

        smtp.quit()
        # print("Send End！")
        return ret
    except Exception as e:
        print(e)
        ret = False
if __name__ == '__main__':
    ret=send_email()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")