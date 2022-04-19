import requests


class Config:
    webhook_url = '<your webhook url>'
    nas_name = '<your nas name>'
    lang = 'kr'


data_kr = {
    'content':f'{Config.nas_name}가 꺼졌습니다.',
    'username':'NAS 알림'
}

data_en = {
    'content':f'{Config.nas_name} is turned off',
    'username':'NAS Notifier'
}

langdata = {'kr':data_kr, 'en':data_en}

webhook_result = requests.post(Config.webhook_url, json=langdata[Config.lang])