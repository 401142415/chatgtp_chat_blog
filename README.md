# 介绍
![Quicker_20230414_151831.png](..%2F..%2FUsers%2FAdministrator%2FDesktop%2FQuicker_20230414_151831.png)

基于django框架
+ 1、django原生的登录、注册
+ 2、写文章，并进行增删查改，暂不支持多媒体
+ 3、实现chatgpt聊天对话功能
+ 4、聊天内进行聊天次数充值、每次聊天扣除聊天次数

# 感谢
+ 前端页面参考[slippersheepig
/
chatgpt-html](https://github.com/slippersheepig/chatgpt-html)
+ 后台调用[lss233
/
chatgpt-mirai-qq-bot](https://github.com/lss233/chatgpt-mirai-qq-bot)的http接口进行聊天
+ 感谢chatgpt给了建议，虽然毫无用处

# 使用事项
+ 1、需要启动redis服务，请在chatgpt.setting.py 中更改REDIS_URL设置
+ 2、需要启动celery服务，请在chatgpt.setting.py 中，更改celery配置
+ 3、需要启动 chatgpt-mirai-qq-bot，请在bots.tasks.py中的gptHttp方法更改配置
+ 4、订单相关我调用了自己的另一个系统，请重写bots中checkOrder.py 与 tasks.py中相关方法