# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:38:22 2023

@author: USER
"""


import requests
import json

url = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'

data = requests.get(url).text  # stream 串流，所以要加上.text

# print(data)

air = json.loads(data) #轉json格式(印出來與data一樣)

# print(air)

air = air['records'] #覆蓋要得K:V 至air

county = {}

#需要的樣子為{'基隆市': [{'sitename': '基隆', 'aqi': '15'}]
#該如何設定
for row in air:
    area = county.get(row['county'])
    
    if area == None:
        temp = list() #為所需要的第一個串列
        sdict = dict() #為所需要的第二個字典
        sdict['sitename'] = row['sitename']
        sdict['aqi'] = row['aqi']
        temp.append(sdict)
        county[row['county']] = temp
       
        
    else:
        sdict = dict() 
        sdict['sitename'] = row['sitename']
        sdict['aqi'] = row['aqi']
        area.append(sdict)
       
        
        
# print(county)



#作業 顯示 縣市:XXX 區域:XXX aqi:XXX 
for item in county:
    print('縣市:', item)
    
    for data in county[item]:
        print('區域:', data['sitename'], 'aqi:', data['aqi'])
    print()
    
