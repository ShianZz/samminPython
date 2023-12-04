# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 21:10:49 2023

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:31:44 2023

@author: USER
"""

import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import db

def Goods(category, products, sale_time):
    print(f"---------{category}---------")
    for p in products:
        link = p['url']
        price_origin = p['price']['origin']
        price_onsale = p['price']['onsale']
        photo = p['image']
        title = p['name'] + p['slogan']
        
        # 將特賣時間加入到標題中
        title_with_time = f"{title} (特賣日期為{sale_time})"
        
        print('網址:', link)
        print('原價:', price_origin)
        print('特價價格:', price_onsale)
        print('相片來源:', photo)
        print('標題:', title_with_time)
        print()
        
        sql ="select * from product where name='{}'".format(title)
                
        db.cur.execute(sql)
        
        res = db.cur.fetchone()
        if res == None:
            sql = "insert into product(name,price_A,price_B,photo_url,link_url) values('{}','{}','{}','{}','{}')".format(title_with_time,price_origin,price_onsale,photo,link)
            
            db.cur.execute(sql)
            db.conn.commit()


today = datetime.today()
today = today.strftime("%Y-%m-%d")

url = "https://ecapi-cdn.pchome.com.tw/fsapi/cms/onsale"

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

pchome = requests.get(url, headers=header).text

data = json.loads(pchome)
# print(data)

onsale = data['data']

for item in onsale:
    category = item['status']
    goods = item['products']

    if category == 'now':
        sale_time = f"{item['startTime']} 至 {item['endTime']}"
        print(f'特賣時間為 {sale_time}')
        Goods(category, goods, sale_time)

    elif category == 'ready':
        sale_time = f"{item['startTime']} 至 {item['endTime']}"
        print(f'特賣時間為 {sale_time}')
        Goods(category, goods, sale_time)

    elif category == 'tomorrow':
        sale_time = f"{item['startTime']} 至 {item['endTime']}"
        print(f'特賣時間為 {sale_time}')
        Goods(category, goods, sale_time)

        