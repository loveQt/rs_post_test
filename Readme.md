#rs_post\_test
##介绍
rs_post_test使用python2.7编写，用来模拟登陆睿思并发贴。最近比较忙，没有时间完善代码。

大概的目标是从贴子列表找提取出带有金币的帖子，然后自动发帖。提取金币贴地址已经完成；发帖测试成功；代码功能不完善。

几个要点：登陆；正则筛选出金币贴地址；formhash的获取和设置
###仅用作学习练习。请勿恶意水贴，一切使用者后果自负。爱护睿思是每个RSer的责任。
##依赖
* 使用requests实现http请求
* 使用Beautiful Soup 4解析返回的html文档

如果缺少依赖的库可以使用pip命令进行安装。
##联系我
* 知乎： [@段晓晨](http://www.zhihu.com/people/loveQt)
* email： [shmilydxc@vip.qq.com](mailto:shmilydxc@vip.qq.com)
