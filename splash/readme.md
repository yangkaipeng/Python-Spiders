1. 安装（需要先安装docker）
    docker pull scrapinghub/splash    (下载splash image到本地)
    docker run -p 8050:8050 scrapinghub/splash  (开启容器，并将本地的端口映射到容器的端口)

2. 执行完上述两条命令后，可以在本地127.0.0.1:8050端口可视化查看splash操作

3. Splash功能丰富，包含多个服务端点
 1). render.html端点 ， JavaScript页面渲染服务
    具体参见： https://www.jianshu.com/p/2b04f5eb5785 
 2). execute端点 自定义js动作
    具体参见： https://www.jianshu.com/p/2b04f5eb5785 

4. scrapy-splash用法：
    见：https://github.com/scrapy-plugins/scrapy-splash

5. 网易云项目流程说明
    先在本地127.0.0.1:8050端口，编写好lua脚本
    脚本实现的功能：
      1.屏蔽图片的加载，对url发送请求
      2.分别定义一个滚动滑条和测量视窗高度的方法
      3.循环向下滚动滑条，直到出现“点击更多”的按钮，触发点击事件
      4.直到出现“已经到最后啦”的提示，退出循环
      5.等待1秒加载完毕之后，返回html
    参考https://github.com/scrapy-plugins/scrapy-splash 完成对scrapy settings文件的修改
    调用scrapy_splash的方法SplashRequest方法，使用endpoit="execute",完成对页面的请求操作
    最后在parse方法中接收的response既是lua脚本返回的html（储存数据等后续工作省去）
    注意，在整个scrapy运行期间，需要开启docker的相关服务，不然无法调用splash进行渲染

6. 更多splash相关操作，请直接啃：
    https://splash.readthedocs.io/en/latest/