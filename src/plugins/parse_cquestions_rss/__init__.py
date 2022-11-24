import feedparser, pickle

from nonebot import get_bot, require
from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler


########将以下内容修改为你自己站点的信息########
check_interval = "*/5" 
#每几分钟检查一次，默认为5

q2a_site_rss_addr = 'http://xxxx.xx/index.php?qa=feed&qa_1=questions.rss' 
#站点新问题RSS地址，若无需要的RSS Feed，请在Q2A管理员设置中打开

q2a_site_name = 'Q&A' 
#站点名称

qusr_id = '' 
#要发送到的个人用户的QQ号，如不需要可留空

qgroup_id = '' 
#要发送到的QQ群号，如不需要可留空
#############################################


@scheduler.scheduled_job("cron", minute=check_interval, id="xxx", args=[1], kwargs={"arg2": 2})
async def run_task(arg1, arg2):

    with open ("prev_questions_list.pkl", 'rb') as f:
        prev_questions_list = pickle.load(f)


    bot = get_bot()

    rss_cquestions = feedparser.parse(q2a_site_rss_addr)
    now_questions_list = [{'title': entry['title'], 'link':entry['link'].split('&')[0], 'pubDate':entry['updated']} for entry in rss_cquestions['entries']]


    for i in now_questions_list:
        is_existed = False
        for j in prev_questions_list:
            if i['link'] == j['link']:
                is_existed = True
        if not is_existed:
            if qusr_id != '':
                await bot.send_msg(message = '{} 发布了新的问题：\n{}\n{}'.format(q2a_site_name, i['title'], i['link']), user_id = qusr_id)
            if qgroup_id != '':
                await bot.send_msg(message = '{} 发布了新的问题：\n{}\n{}'.format(q2a_site_name, i['title'], i['link']), group_id = qgroup_id)
            prev_questions_list.append(i)


    with open ("prev_questions_list.pkl", 'wb') as f: 
        pickle.dump(prev_questions_list, f)
