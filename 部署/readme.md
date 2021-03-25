部署流程：

需要用到scrapyd和scrapyd-client
前者以http命令方式发布、删除、启动、停止爬虫程序，实现可视化
后者将爬虫文件打包成egg文件并将代码上传到服务器中


1.安装scrapyd 和 scrapyd-client
pip install scrapyd
pip install scrapyd-client

2.修改cfg文件
将url改成要部署的服务器的公网IP
[deploy]
url = http://localhost:6800/         本地部署

3.开启scrapyd
命令行输入 scrapyd

4.开始部署
scrapyd-deploy -p demo(项目名称)

5.开启爬虫
curl http://localhost:6800/schedule.json -d project=demo -d spider=mydemo

6.关闭爬虫
curl http://localhost:6800/cancel.json -d project=demo -d job='jobid'

7.其他常用操作
获取部署的爬虫列表
curl http://localhost:6800/listprojects.json

获取项目下的爬虫文件列表
curl http://localhost:6800/listspiders.json?project=demo

获取工程下的爬虫运行状态
curl http://localhost:6800/listjobs.json?project=demo

删除部署的爬虫项目
curl http://localhost:6800/delproject.json -d project=demo

8.远程部署
    1).将cfg中的url改为远程的IP
       url = http://远程服务器IP:6800/ 
    2).在远程服务器上安装好所有需要用到的库，包括scrapyd和scrapyd-client
    3).修改scrapyd的配置文件，允许外网访问 
        查找配置文件的路径：find -name default_scrapyd.conf
        修改配置文件: sudo vim 路径
        将参数bind_address 改为0.0.0.0
    4).远程服务器配置安全组，设置允许6800端口访问
    5).部署命令和本地一样（见步骤4）
    6).在本地浏览器输入 远程服务器IP:6800 访问。其他操作做相应修改即可
