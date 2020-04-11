#coding = utf-8

__author__ = "LT"
__title__ = "公共函数类工具类"
__desc__ = """公共函数工具类"""

import random
import socket
import os
import datetime

# ---------------------------------------------公共常量定义 start ----------------
SUCCESS = "pass"
FAIL = "fail"
# 响应结果定义 结果和描述信息 响应码，状态 success/fail,描述信息
resp={'code':'200','result':SUCCESS,'msg':''}

# ---------------------------------------------公共常量定义 end ----------------

# ---------------------------------------------公共函数定义 start ----------------
def getIp():
    '''获取本机ip地址'''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
    except:
        ip = "fail"
    return ip

def getPhoneNumber():
    ''' phone number 需要正确的手机号测试验证码'''
    prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
    return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))

def getCard():
    '''card number '''
    return "303"+"".join(random.choice("0123456789") for i in range(13))

def getIdCard():
    ''' idcard number'''
    month=random.randint(1,12)
    if month<10:
        month="0"+str(month)
    else:
        month=str(month)
    day=random.randint(1,30)
    if day<10:
        day="0"+str(day)
    else:
        day=str(day)
    idcard="511623"+str(random.randint(1958,1996))+month+day+str(random.randint(1000,9999))
    return idcard

def createFileDirs(logDir=""):
    '''创建日志文件夹'''
    # 年-月-日
    dayTime = datetime.datetime.now().strftime('%Y-%m-%d')
    # 时:分:秒
    hourTime = datetime.datetime.now().strftime('%H%M%S')
    if logDir=="":
        logDir =os.getcwd()
    targetDir = logDir + '/' + dayTime + '/' + hourTime
    # 判断文件夹是否已存在
    isExists = os.path.exists(targetDir)
    if not isExists:
        os.makedirs(targetDir)
    return targetDir    
# ---------------------------------------------公共函数定义 end ----------------


# 私有方法内部启动测试
if __name__ == '__main__':
    getIdCard()
