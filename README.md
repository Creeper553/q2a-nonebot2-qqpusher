# q2a-nonebot2-qqpusher
基于 Nonebot2 的 Question2Answer 新问题 QQ 推送机器人 / A Question2Answer new question QQ pusher based on Nonebot2.

![image.png](https://attachment.mcbbs.net/public/resource/8b198dc7-a0f8-4258-b9b1-b198204e64da.png)

## 使用

1. 安装 Python 环境。使用的 Nonebot2 框架要求 Python 版本 >= 3.8，实测使用 Python 3.11 安装 Nonebot2 时有部分依赖需要本机编译，会发生很麻烦的问题，因此建议使用 3.9 或 3.10。Debian 11.3 自带的 Python 3.9 实测无问题，或可参考 https://www.cnblogs.com/STangQL/p/15647583.html。

2. 安装 Nonebot2 脚手架。建议使用：

   `pip install nb-cli`

   安装后使用指令 `nb` 检查是否安装成功，能看到输出的 logo 即可。

   也可通过 `pip install nonebot2` 手动安装。如遇其他问题请参见 [Nonebot2 官网](https://nb2.baka.icu/docs/)。

3. 安装插件运行所需要的依赖。Bot 正常运行需要使用 onebot v11 的适配器，RSS 解析使用了 feedparser，定时检查站点使用了 APScheduler。

   适配器可通过输入 nb 指令后按步骤安装：

   ```
   Welcome to NoneBot CLI!
   
   [?] What do you want to do? Adapter ->
   [?] What do you want to do? Install a Published Adapter
   [?] Adapter name you want to install? v11
   
   Looking in indexes: http://mirrors.cloud.aliyuncs.com/pypi/simple/
   ...
   ```

   依赖可使用以下指令安装：

   `nb plugin install nonebot-plugin-apscheduler`

   `pip install feedparser`

4. 将 `c-question-bot-core`（机器人核心） 和 `go-cqhttp_linux_amd64`（gocq） 两文件夹上传到服务器。为保证 QQ 帐号能够正常登录，需要一台与手机处在同一局域网下的设备。此处也提供了一份 windows 下的 gocq 供稍后登录使用（具体步骤在后面）。

   Bot 使用端口 15687 与实现端通信，请检查此端口是否被占用，也可在核心下的 `.env.dev` 文件里修改 PORT 字段，并修改 gocq 配置文件 `config.yml` 的 `servers:` -> `- ws-reverse:` -> `universal:` 下使用的端口（此处已配置好使用反向ws），保持一致。

5. 修改机器人核心部分：将 `src/plugins/parse_cquestions_rss/__init__.py` 中的配置信息修改为站点的对应信息，这里提供的文件直接来自生产环境，具体需要修改的部分及含义，请见文件内注释（我懒了qwq，没用 config）。

   信息修改完成后，在 `bot.py` 所在路径下运行 `nb run` 启动机器人核心。

6. 配置 go-cqhttp 并登录需要使用的 QQ 账号：修改 `config.yml` 中 `account` -> `uin` 中的 QQ 号，改成用来当作机器人的 QQ 账号。密码可填可不填，填了也没用。因为 QQ 的风险控制策略，直接在服务器上登录 QQ 账号会提示风险警告，无法正常登录。解决方法：先使用手机 QQ 登录当作机器人的账号，将一台电脑与手机处在同一局域网下，把改过的 `config.yml` 粘贴到那台本地机子的 gocq 文件夹中，先在本地运行 go-cqhttp.bat （我们假设这台机子是windows），gocq会打印一张二维码，使用手机扫码进行本地登录。本地登录成功后，将生成的 device.json 和 session.token 粘贴到服务器中，重新运行 `./go-cqhttp` 登录启动服务；具体步骤详见 [官方文档](https://docs.go-cqhttp.org/guide/#go-cqhttp)。

7. 如无异常，gocq 会打印已连接到反向ws服务器的信息。提供的文件保留了内置的 echo 插件，可私聊机器人发送 `/echo <message>` 消息检验机器人是否运行正常；若正常，机器人会重复你发送过去的消息。此时机器人应该已经在正常运行了。
