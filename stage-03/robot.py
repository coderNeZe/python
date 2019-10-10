import datetime
import time,os
from apscheduler.schedulers.background import BackgroundScheduler
#import pysnooper
import requests,json

headers = {"Content-Type": "application/x-www-form-urlencoded"}
# 机器人发送消息的webhook地址
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=76fa0154-5fd1-4eb3-b4b0-f51b2dfcaaa4"


def send_order_message():
    content="美女们，订饭了！@all"
    data = {"msgtype": "text", "text": {
        "content": content}}
    res = requests.post(url, data=json.dumps(data), headers=headers)

def send_week_report():
    content="周报，我好辛苦！天天操心，@all"
    data = {"msgtype": "text", "text": {
        "content": content}}
    res = requests.post(url, data=json.dumps(data), headers=headers)


def send_morning_remind():
    content="早会，@all"
    data = {"msgtype": "text", "text": {
        "content": content}}
    res = requests.post(url, data=json.dumps(data), headers=headers)



def send_rest_message():
    content="美女们，注意休息喝水哦！，@all"
    data = {"msgtype": "text", "text": {
        "content": content}}
    res = requests.post(url, data=json.dumps(data), headers=headers)


if __name__ == '__main__':
    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()
    # 添加调度任务
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
    # scheduler.add_job(send_week_report, 'interval',second=2)
    scheduler.add_job(send_week_report,'cron',day_of_week='thu',hour=17,minute=30)
    scheduler.add_job(send_morning_remind,'corn',day_of_week='mon-fri',hour=9,minute=30)
    scheduler.add_job(send_order_message,'corn',day_of_week='mon-fri',hour=15,minute=30)
    scheduler.add_job(send_rest_message, 'corn', day_of_week='mon-fri', hour='10-12,14-21', minute=30)
    # 启动调度任务
    scheduler.start()

    # while True:
    #     print(time.time())
    #     time.sleep(5)