# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 00:21:49 2023

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import time
import db

print(db.conn)


url="https://news.tvbs.com.tw/travel"

data = requests.get(url).text

soup = BeautifulSoup(data,'html.parser')

foodslist = soup.find('div',class_ ='news_now2')

allfoods = foodslist.find('div',class_='list')

foods = allfoods.find_all('li')
# print(foods)
i=0
for item in foods:
    adata = item.find('a')
    if not(adata == None):
        link = 'https://news.tvbs.com.tw' + adata.get('href')      
        img = adata.find('img').get('data-original')
        title = adata.find('h2').text
        fdate = adata.find('div',class_='time').text

        i+=1
        print(title)
        print(img)
        print(fdate)
        print(link)
        print()
        
        
        if i == 50:
            break
        
        try:
            sql = "SELECT * FROM tvfoods WHERE title = '{}' ORDER BY id DESC".format(title)
            db.cur.execute(sql)
            res = db.cur.fetchone()
            if res is None:
                sql = "INSERT INTO tvfoods (title, photo_url, fdate, flink) VALUES (%s, %s, %s, %s)"
                values = (title, img, fdate, link)
        
                db.cur.execute(sql, values)
                db.conn.commit()
                print("成功寫入資料庫")
            else:
                print("新聞已存在，不寫入資料庫")

        except Exception as e:
            print(f"錯誤：{e}")
                
            
    
    time.sleep(0.5)
db.conn.close()




