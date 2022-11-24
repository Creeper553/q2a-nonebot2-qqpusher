# q2a-nonebot2-qqpusher
基于 Nonebot2 的 Question2Answer 新问题 QQ 推送机器人 / A Question2Answer new question QQ pusher based on Nonebot2.

## 使用

配置运行环境。推荐使用 Python 3.10 作为 Nonebot2 的运行环境。

1. 安装 Python 3.10。

2. 安装 Nonebot2 脚手架

   `pip install nb-cli`

   或者通过 `pip install nonebot2` 手动安装。详见 [Nonebot2 官网](https://nb2.baka.icu/docs/)。

3. 安装插件运行所需要的依赖。RSS 解析使用了 feedparser，定时检查站点使用了 APScheduler。

   使用以下指令安装：

   `nb plugin install nonebot-plugin-apscheduler`

   `pip install feedparser`

4. 将 `src/plugins/parse_cquestions_rss/__init__.py` 中的配置信息修改为你自己站点的对应信息。

5. 配置 OneBot v11 实现。推荐使用 go-cqhttp。下载 go-cqhttp 在你需要运行平台上的 [发行版本](https://github.com/Mrs4s/go-cqhttp/releases)，运行，使用反向 WebSocket 服务器模式，并按照指示，登录作为机器人的 QQ 账号。详见 [官方文档](https://docs.go-cqhttp.org/guide/#go-cqhttp)。

6. 回到 `bot.py` 所在的文件夹，使用 `nb run` 运行 Nonebot 机器人，并配置 Nonebot2 与 go-cqhttp 使用的端口号等信息，使二者能够成功连接。

7. 完成。

