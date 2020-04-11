#coding = utf-8

__author__ = "LT"
__title__ = "启动入口"
__desc__ = """启动入口程序模块"""

from airtest.core.api import using

using("myconfig.air")
from myconfig import start_model
#-----------------------生产启动函数---------------------------------
def start_prod():
    '''生产模式启动'''
    # 引入启动模块
    using("businessdao.air")
    from businessdao import run
    # 调用启动方法
    run()
    
print("-----------------------主启动程序---------------------->start_run start")
if start_model == "prod":
    start_prod()
else:
    print("请检查myconfig配置中启动模式是否改为prod模式")    
print("-----------------------主启动程序---------------------->start_run end")