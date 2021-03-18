
分布式爬取医院名称及链接


1.所需lib
    scrapy-redis
    user_agent
    
2.需安装redis数据库

3.需拷贝一份代码到其他服务器，且配置文件中的REDIS_HOST要和主服务器的保持一致

运行方法：
 step 1:  
    分别在主从服务器上执行命令行：python run.py
 step 2:
    主服务器启动redis数据库，运行: lpush hospital:start_urls http://z.xywy.com/
 
