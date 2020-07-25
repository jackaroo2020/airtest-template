# airtest-template
#### 第一章	运行环境搭建 <br/>    
1、python 安装      
本地开发环境python版本为：3.6，建议下载此版本
搭建参考：
https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624

2、AritestIDE 安装           
本地开发环境AirtestIDE版本为：V1.2.3,建议下载此版本
搭建参考：
https://airtest.doc.io.netease.com/IDEdocs/getting_started/AirtestIDE_install/

3、mysql 安装           
本地开发环境mysql版本为：5.7.26,建议下载安装5.7版本以上即可
搭建参考：
https://blog.csdn.net/qq3399013670/article/details/97386205     

#### 第二章、UI框架配置说明（*****） <br/>     
1、框架结构       
![avatar](/mydoc/images/1.png)

* businessdao.air: 提供用例场景运行日志插入与更新数据库操作
* commonutils.air: 提供公共的工具类函数，如自动生成手机号，身份证号，ip等函数
* dbutils.air: 提供数据库连接池和基本的增删改查模版函数
* myconfig.air: 提供数据库配置、全局参数，如是否开启自动生成报告，业务参数的配置
* mycases.air: 提供某个业务的所有用例场景，可以根据项目大小灵活拆分。
* startrun.air: 项目的启动入口，运行此模块会自动加载businessdao.air模块下的run函数，run函数会查询数据库需要执行的用例，批量顺序执行测试用例。

2、运行环境依赖配置
* 项目启动python环境需要安装pymysql,DButils第三方模块，安装前切换镜像源：       
将pip源更换到国内镜像。用pip管理工具安装库文件时，默认使用国外的源文件，因此在国内的下载速度会比较慢，可能只有50KB/s。      
阿里云: https://mirrors.aliyun.com/pypi/simple/ <br/>     
中国科技大学: https://pypi.mirrors.ustc.edu.cn/simple/<br/> 
清华大学: https://pypi.tuna.tsinghua.edu.cn/simple/<br/> 
临时方法：<br/> 
pip install 模块名称 -i 镜像源，如：<br/> 
pip install pymysql -i https://mirrors.aliyun.com/pypi/simple/<br/> 
pip install DButils -i https://mirrors.aliyun.com/pypi/simple/<br/> 
永久方法：<br/> 
windows文件管理器下输入：%APPDATA%<br/> 
新建pip文件夹，在pip文件夹下新建pip.ini文件<br/> 
输入如下代码并保存：<br/> 
[global]<br/> 
index-url = https://pypi.tuna.tsinghua.edu.cn/simple/<br/> 
[install]<br/> 
trusted-host=pypi.tuna.tsinghua.edu.cn<br/> 
然后：<br/> 
pip install pymysql  <br/> 
pip install DBUtils<br/> 

3、启动需要注意的配置细节（******）<br/> 
* 需要配置python自定义环境。AirtestIDE配置参考图如下：<br/> 
<img src="./mydoc/images/2.png" width = "700"  /><br/>
<!-- ![avatar](/mydoc/images/2.png) -->

* myconfig.air 数据库配置参考图如下：<br/> 
<img src="./mydoc/images/3.png" width = "700"  /><br/>

4、 数据库表结构，运行前需要初始化表结构，并在ui_case表中初始化用例场景初始化信	息（******）。<br/> 

#### 第三章、启动说明<br/> 
1、 启动方式一(******)<br/> 
(1)打开myconfig.air,修改启模式为prod:   start_model=”prod”<br/> 
(2)运行startrun.air模块，此模块将加载bussinessdao.air模块下的run方法。从数据库选择需要运行的测试用例。数据库表的配置详见第二章数据库表设计及说明。<br/> 
<img src="./mydoc/images/4.png" width = "700"  /><br/>

2、 启动方式二<br/> 
打开myconfig.air,修改启模式为dev:   start_model=”dev”<br/> 
<img src="./mydoc/images/5.png" width = "700"  /><br/>

#### 第四章、常见问题<br/> 
1、手机连接不上，参考官网尝试解决：<br/> 
https://airtest.doc.io.netease.<br/> com/IDEdocs/device_connection/2_android_faq/<br/> 

#### 第五章、使用说明书及视频演示资料(服务收费版(19.9元)
以下为脚手架整理的全部资料，供参考，如需资料，请关注个人微信公众号，获取详细内容<br/> 
公众号：<br/> 
<img src="./mydoc/images/gzh.jpg" width = "200" height = "200" /><br/> 
资料部分截图如下所示：<br/>
<img src="./mydoc/images/pay_1.png" width = "500"  /><br/>
<img src="./mydoc/images/pay_2.png" width = "500"  /><br/>
<img src="./mydoc/images/pay_3.png" width = "500"  /><br/>
<img src="./mydoc/images/pay_4.png" width = "500"  /><br/>
<img src="./mydoc/images/pay_5.png" width = "500"  /><br/>

#### 支持
该项目是个人基于Airtest搭建的模块框架，如有不足之处，欢迎指正。如果对你有帮助，麻烦给个 star 哟👏👏


