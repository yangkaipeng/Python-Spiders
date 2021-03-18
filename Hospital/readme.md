
分布式爬取医院名称及链接


1.所需lib
    scrapy-redis
    user_agent
    
2.需安装redis数据库

运行方法：
 step 1:  
    命令行运行：python run.py
 step 2:
    启动redis数据库，运行 lpush hospital:start_urls http://z.xywy.com/
 
