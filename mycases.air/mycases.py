#coding = utf-8

__author__ = "LT"
__title__ = "场景用例"
__desc__ = """我的所有测试场景用例集"""

# -------------------------引入依赖 start-------------------------------------------------------------
from airtest.core.api import *
import traceback
import os

using("commonutils.air")
from commonutils import SUCCESS,FAIL,resp,createFileDirs
using("myconfig.air")
from myconfig import *

# 初始化定义
auto_report_Flag = False

# 是否自定义日志目录，自定义日志目录，则自动生成报告在当前目录下
if len(logDir) > 0:
    # auto_setup(basedir=None, devices=None, logdir=None, project_root=None, compress=0)[源代码]
    targetLodDir = createFileDirs(logDir)
    # 当前目录
    root_dir = os.getcwd()
    print("创建执行日志目录----------》",targetLodDir)
    auto_setup(__file__,logdir=targetLodDir)
    # 自动生成报告打开标志位
    auto_report_Flag = True
else:
    auto_setup(__file__) # 保持默认参数
    
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# -------------------------引入依赖 end---------------------------------------------------------------


# -------------------------公共常量 start-------------------------------------------------------------
print("logDir: %s" % (logDir))
# -------------------------公共常量  end----------------------------------------------------------------


# -------------------------公共函数 start----------------------------------------------------------------
def auto_generate_report(auto_report_Flag):
    '''自动生成报告'''
    if auto_report_Flag:
        print("auto_generate_report--------------start")
        # generate html report
        from airtest.report.report import simple_report
        #生成报告目录
        output_file = targetLodDir + '/log.html'
        #生成报告的方法
        simple_report(root_dir, logpath=targetLodDir, output=output_file)
        print("auto_generate_report--------------end")

def restartApp(appname="com.google.android.calculator",timeout=2):
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
    '''01 [APP】test (1+2)==3'''
    resp["result"] = FAIL
    try:
        # test (1+2)==3
        poco("com.google.android.calculator:id/digit_1").click()
        poco("com.google.android.calculator:id/op_add").click()
        poco("com.google.android.calculator:id/digit_2").click()
        poco("com.google.android.calculator:id/eq").click()
        result = poco("com.google.android.calculator:id/result").get_text()
        assert_equal(result, "3")

        ## test swipe
        poco("com.google.android.calculator:id/arrow").click()
        sleep(1.0)
        fun_log = poco("com.google.android.calculator:id/fun_log").exists()
        assert_equal(fun_log, True)
        poco("com.google.android.calculator:id/arrow").swipe([0.6884, 0.01])
        sleep(1.0)

        ## touch all numbers for fun
        poco("com.google.android.calculator:id/clr").click()
        for btn in poco(nameMatches="com.google.android.calculator:id/digit_\d"):
            print(btn)
            btn.click()

        result2 = poco("com.google.android.calculator:id/formula").get_text()
        assert_equal(result2, "7894561230")
        
        # 响应成功
        success(method="case_01")
    except:
        error(method="case_01")
    # 重启应用
    restartApp()  
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
        if not SUCCESS == resp.get('result',"-1"):
            fail = fail +1
        print(method+"():用例场景------------------>运行结束，结果为："+resp.get('result',"-1")) 
        log(method+"():用例场景------------------>运行结束，结果为："+resp.get('result',"-1")) 
    print("所有的用例场景------------------>运行结束,运行总数为：%s, 失败个数为：%s" % (count,fail))
    log("所有的用例场景------------------>运行结束,运行总数为：%s, 失败个数为：%s" % (count,fail))# 报告展示使用
    
# 用例调试模式启动运行，从start_run启动时候，需要注销此
if start_model=="dev":
    print("启动模式为dev模式")
    test_uicase()
    # 自动生成报告  自定义日志目录，则自动生成
    auto_generate_report(auto_report_Flag)
elif start_model=="prod":
    print("启动模式为prod模式")
else:
    print("请检查myconfig配置中启动模式是为prod或者dev启动模式")   
# ---------------------------测试函数 end---------------------------------------------------------



