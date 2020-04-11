#coding = utf-8

__author__ = "LT"
__title__ = "业务测试用例数据库操作记录模版库"
__desc__ = """业务测试用例启动运行操作记录到数据库函数操作记录模版库"""

from airtest.core.api import *

# 引入需要执行用例的测试场景用例
using("mycases.air")
from mycases import *
using("dbutils.air")
from dbutils import *
using("commonutils.air")
from commonutils import getIp,SUCCESS,FAIL
using("myconfig.air")
from myconfig import CLASSIFY

import datetime
import traceback

# -------------------------公共常量 start start--------------------------------------
# 方法参数集合
# methodsTuple = methodsTuple
# -------------------------公共常量 end------------------------------------------------

# 获取执行的用例列表  根据标识
def fetchUiCaseALL(classify):
    sql =  "SELECT case_id,case_desc,method,exp_result FROM ui_case WHERE classify = %s and implement = 'Y' ORDER BY sort"
    return select_all(sql, [classify])

# 获取执行用例的总数
def fetchUiCaseTotal(classify):
    return len(fetchUiCaseALL(classify))

# 插入主表日志
def insertLog(startTime,total,operationIp):
    sql = "insert into ui_log(start_time,sum,operation_ip) VALUE (%s,%s,%s)"
    return insert_one_pk(sql,[startTime,total,operationIp])
    
# 更新日志主表信息    
def updateLog(*args):
    sql = " update ui_log set end_time=%s ,total_time=%s, success=%s, success_rate=%s where log_id=%s"
    return update_one(sql,args)

# 插入日志详细表信息
def insertDetailLog(*args):
    sql = "insert into ui_detail_log(log_id,case_id,start_time,end_time,total_time,exp_result,act_result,result_desc) VALUE (%s,%s,%s,%s,%s,%s,%s,%s)"
    return insert_one(sql,args)

# 封装更新日志表参数)
# update ui_log set end_time=%s ,total_time = %s, success = %s,  success_rate = %s where log_id = %s
def getUpdateLogParams(t1,total,success,logId):
    t2 = datetime.datetime.now()
    # 结束时间
    endTime = datetime.datetime.strftime(t2, '%Y-%m-%d %H:%M:%S')
    # 总时间
    totalTime = (t2 -t1).seconds
    # 成功率
    successRate = '{:.2%}'.format(success/total)
    # 元参数，顺序与sql对应，不能随意更改
    return (endTime,totalTime,success,successRate,logId)

# 用例执行日志
def insertCaseLog(logId,caseId,t3,t3StrTime,expResult,resp):
    t4 = datetime.datetime.now()
    t4StrTime = datetime.datetime.strftime(t4, '%Y-%m-%d %H:%M:%S')
    # 单个用例执行总时间
    t34ToalTime = (t4 -t3).seconds
    # 封装详细日志参数 insert into ui_detail_log(log_id,case_id,start_time,end_time,total_time,exp_result,act_result,result_desc)    
    detailParams = (logId,caseId,t3StrTime,t4StrTime,t34ToalTime,expResult,resp.get('result'),resp.get('msg',''))
    # 记录详细日志信息  
    insertDetailLog(*detailParams)

# 运行函数
def run():
    # 记录主日志表
    t1 = datetime.datetime.now()
    startTime = datetime.datetime.strftime(t1, '%Y-%m-%d %H:%M:%S')
    # 执行的总用例数
    total = fetchUiCaseTotal(CLASSIFY)
    # 操作的ip地址
    operationIp = getIp()
    logId = insertLog(startTime,total,operationIp)
    # 初始化成功数
    success = 0 
    # 获取要执行的所有用例场景  
    results = fetchUiCaseALL(CLASSIFY) 
    for row in results:
        # 用例信息
        caseId = row.get('case_id',-1)
        method = row.get('method',-1)
        expResult = row.get('exp_result',-1)
        # 查找已调试完成的用例列表进行执行
        if method in methodsTuple:
            print(method+"():用例场景------------------>开始运行")
            log(method+"():用例场景------------------>开始运行") # 报告展示使用
            t3 = datetime.datetime.now()
            t3StrTime = datetime.datetime.strftime(t3, '%Y-%m-%d %H:%M:%S')
            # 执行测试用例
            resp = eval(method+"()")
             # 如果成功，则累计加和
            if SUCCESS == resp.get('result',"-1"):
                 success = success + 1
            # 记录用例执行日志
            insertCaseLog(logId,caseId,t3,t3StrTime,expResult,resp)
            print("\n"+method+"():用例场景------------------>运行结束，运行结果为："+resp.get('result',"-1"))
            log(method+"():用例场景------------------>运行结束，运行结果为："+resp.get('result',"-1"))# 报告展示使用
        else:
            print(method+"():用例场景------------------>找不到对应的用例，请检查测试用例method名称是否填写正确")
            log(method+"():用例场景------------------>找不到对应的用例，请检查测试用例method名称是否填写正确")# 报告展示使用
            t3 = datetime.datetime.now()
            t3StrTime = datetime.datetime.strftime(t3, '%Y-%m-%d %H:%M:%S')
            result_desc = method+"用例场景运行忽略，请检查测试用例method名称是否填写正确"
            # (logId,caseId,t3StrTime,t4StrTime,t34ToalTime,expResult,act_result,result_desc)
            detailParams = (logId,caseId,t3StrTime,t3StrTime,0,expResult,"fail",result_desc)
              # 记录详细日志信息  
            insertDetailLog(*detailParams)   
    # 封装执行结束的元参数列表
    updateLogParams = getUpdateLogParams(t1,total,success,logId)
    # 执行结束更新主日志表信息
    updateLog(*updateLogParams)  
    print("所有的用例场景------------------>运行结束,运行总数为：%s, 失败个数为：%s" % (total,total-success))
    log("所有的用例场景------------------>运行结束,运行总数为：%s, 失败个数为：%s" % (total,total-success))# 报告展示使用
    # 自动生成报告  自定义日志目录，则自动生成
    auto_generate_report(auto_report_Flag)
    

