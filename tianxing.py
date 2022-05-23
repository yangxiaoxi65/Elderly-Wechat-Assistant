# -*- coding: utf-8 -*-
# import http.client, urllib
# conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
# params = urllib.parse.urlencode({'key':'f4888284e6a3c5207613501146b89e5a','city':'上海市'})
# headers = {'Content-type':'application/x-www-form-urlencoded'}
# conn.request('POST','/tianqi/index',params,headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode('utf-8'))

from urllib.parse import urlencode
import requests
import urllib
import json

url="http://api.tianapi.com/tianqi/index?key=f4888284e6a3c5207613501146b89e5a&city=%E4%B8%8A%E6%B5%B7%E5%B8%82"
request=url
re=requests.get(request)
rep = re.json()
'''
获取网页中的响应的元组变量
'''
code = rep.get('code')
msg = rep.get('msg')
area = rep.get('area')
# up = rep.get('update_time')
# wea = rep.get('wea')
# wea_img = rep.get('wea_img')
# tem = rep.get('tem')
# tem_day = rep.get('tem_day')
# tem_night = rep.get('tem_night')
# win = rep.get('win')
# win_speed = rep.get('win_speed')
# win_meter = rep.get('win_meter')
# air = rep.get('air')
# time = rep.get('time')
print('\n城市名字：',area)
# print('更新时间：',up)
# print('天气情况：',wea)
# print('时实温度：',tem)
# print('高温：',tem_day)
# print('低温：',tem_night)
# print('风向：',win)
# print('风力等：',win_speed)
# print('风速：',win_meter)
# print('空气质量：',air)
# print('当天日期，星期：',time,'\n')
lis = {'code':code,
'msg':msg,
# 'city':area,
# 'update_time':up,
# 'wea':wea,
# 'wea_img':wea_img,
# 'tem':tem,
# 'tem_day':tem_day,
# 'win':win,
# 'win_speed':win_speed,
# 'win_meter':win_meter,
# 'air':air,
# 'time':time,
}
print(lis)