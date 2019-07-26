# -*- coding: utf-8 -*-
# 获得天气信息并推送
import requests


def get_origin_info(city_id):
    r = requests.get(f'http://www.weather.com.cn/data/cityinfo/{city_id}.html')
    if r.status_code == 200:
        r.encoding = 'utf-8'
        return r.json()
    else:
        return {}


def parse_info(info_dict):
    if not info_dict:
        return info_dict
    info = info_dict["weatherinfo"]
    return "{city}市今天{weather}, 气温：{temp1}到{temp2}".format(**info)


def create_hookinfo(hook, msg, mentioned_mobile_list):
    data = {
        "msgtype": "text",
        "text": {
            "content": msg,
            "mentioned_list": [],
            "mentioned_mobile_list": mentioned_mobile_list
        }
    }
    requests.post(hook, json=data)

if __name__ == "__main__":
    city_id = "101210101"
    origin_info = get_origin_info(city_id)
    msg = parse_info(origin_info)

    key = "cbd6176e-9f0b-4a78-b8b2-"
    hook = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?{key}"
    mentioned_mobile_list = ["18258261294", "18340818166"]
    create_hookinfo(hook, msg, mentioned_mobile_list)
