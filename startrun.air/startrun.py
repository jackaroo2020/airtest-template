#coding = utf-8

"启动入口程序模块"

__author__ = "LT"

from airtest.core.api import using

using("businessdao.air")
from businessdao import run
using("myconfig.air")
from myconfig import start_model

print("-----------------------主启动程序---------------------->start_run start")
if start_model == "prod":
    run()
else:
    print("请检查myconfig配置中启动模式是否改为prod模式")    
print("-----------------------主启动程序---------------------->start_run end")
    


