import requests


class Config:
    webhook_url = '<your webhook url>'
    nas_name = '<your nas name>'
    lang = 'kr'


data_kr = {
    'content':f'{Config.nas_name}가 꺼졌습니다.',
    'username':'NAS 알림',
    'avatar_url':'https://rawcdn.githack.com/krome0/nas-discord-notifier/b81046852f29a92448db6d605a1a22603f69b7bd/bot_icon.png'
}

data_en = {
    'content':f'{Config.nas_name} is turned off',
    'username':'NAS Notifier',
    'avatar_url':'https://rawcdn.githack.com/krome0/nas-discord-notifier/b81046852f29a92448db6d605a1a22603f69b7bd/bot_icon.png'
}

langdata = {'kr':data_kr, 'en':data_en}

webhook_result = requests.post(Config.webhook_url, json=langdata[Config.lang])