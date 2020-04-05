#coding = utf-8

"我的所有测试场景"

__author__ = "LT"

# -------------------------引入依赖 start-------------------------------------------------------------
from airtest.core.api import *
import traceback
import os

using("commonutils.air")
from commonutils import SUCCESS,FAIL,resp,createFileDirs
using("myconfig.air")
from myconfig import logDir, auto_report_Flag,start_model,case_01_params

# auto_setup(basedir=None, devices=None, logdir=None, project_root=None, compress=0)[源代码]
targetLodDir = createFileDirs(logDir)
# 当前目录
root_dir = os.getcwd()
print("创建执行日志目录----------》",targetLodDir)
auto_setup(__file__,logdir=targetLodDir)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# -------------------------引入依赖 end---------------------------------------------------------------


# -------------------------公共常量 start-------------------------------------------------------------
print("auto_report_Flag: %s" % (auto_report_Flag))
# -------------------------公共常量  end----------------------------------------------------------------


# -------------------------公共函数 start----------------------------------------------------------------
def auto_generate_report(auto_report_Flag=False):
    '''自动生成报告'''
    if auto_generate_report==True:
        print("auto_generate_report--------------start")
        # generate html report
        from airtest.report.report import simple_report
        #生成报告目录
        output_file = targetLodDir + '/log.html'
        #生成报告的方法
        simple_report(root_dir, logpath=targetLodDir, output=output_file)
        print("auto_generate_report--------------end")

def restartApp(appname="",timeout=5):
    '''重启应用'''
    stop_app(appname)
    start_app(appname)
    sleep(timeout)

def success(method=""):
    '''成功响应封装函数'''
    resp['result'] = SUCCESS
    resp['msg'] = method+"： 执行成功"

def error(method=""):
    '''异常封装函数'''
    resp['msg'] = traceback. format_exc() # 记录到数据库使用
    print(method+": "+FAIL, traceback. format_exc()) # 调试打印使用
    log("出错啦："+method, traceback. format_exc()) # 报告展示使用

# -------------------------公共函数 end--------------------------------------------------------------------


# -------------------------测试场景用例 start--------------------------------------------------------------------
def case_01():
    '''01 [H5】未注册的用户输入正确的验证码进行注册，注册成功'''
    resp["result"] = FAIL
    try:
        # step1: 
        #   
        # 响应成功
        success(method="case_01")
    except:
        error(method="case_01")
    # 重启应用
    # restartApp()  
    return resp


# -------------------------定义  已调试完成的用例列表方法名称 这个在start_run启动时候，与数据库相关操作使用--- start---
# 注意 调试完成一个测试用例，在此添加一个，start_run启动从数据库读取需要执行的用例，需要与此测试用例名称一致
methodsTuple=("case_01")  
# -------------------------定义  已调试完成的用例列表方法名称 这个在start_run启动时候，与数据库相关操作使用--- end---


# -------------------------测试场景用例 end--------------------------------------------------------------------

# -------------------------测试函数 start---------------------------------------------------------------------
# 内部测试使用,调试开发不连接数据库启动使用,启动start_run运行时候得注释此函数
def test_uicase():
    '''内部测试函数'''
    count = 0
    fail = 0
    methodsList = []
    methodsList.append("case_01")
    for method in methodsList:
        count = count +1
        log(method+"():用例场景------------------>开始执行") # 报告展示使用
        print(method+"():用例场景------------------>开始执行") # 报告展示使用
        resp = eval(method+"()")
        if SUCCESS == resp.get('result',"-1"):
        else:
            fail = fail +1
        print(method+"():用例场景------------------>运行结束，结果为："+resp.get('result',"-1")) 
        log(method+"():用例场景------------------>运行结束，结果为："+resp.get('result',"-1")) 
    print("所有的用例场景------------------>运行结束,运行总数为：%s, 失败个数为：%s" % (count,fail))
    log("所有的用例场景------------------>运行结束,运行总数为：%s, 失败个数为：%s" % (count,fail))# 报告展示使用
    
# 用例调试模式启动运行，从start_run启动时候，需要注销此
if start_model=="dev":
    test_uicase()
else:
    print("请检查myconfig配置中启动模式是否改为dev模式")    
# ---------------------------测试函数 end---------------------------------------------------------

# 自动生成报告  可以自选生成与否
auto_generate_report(auto_report_Flag)



