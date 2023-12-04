# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import db

print(db.conn)

today = datetime.today()
today = today.strftime('%Y-%m-%d')

url="https://news.tvbs.com.tw/realtime"

data = requests.get(url).text

soup = BeautifulSoup(data,'html.parser')

newslist = soup.find('div',class_ ='news_list')

allnews = newslist.find('div',class_='list')

news = allnews.find_all('li')

i=0
for item in news:
    adata = item.find('a')
    if not(adata == None):
        link = 'https://news.tvbs.com.tw' + adata.get('href')
        
        img = adata.find('img').get('data-original')
        title = adata.find('h2').text
        
        
        content = requests.get(link).text
        
        sp = BeautifulSoup(content,'html.parser')
        newsinfo = sp.find(id='news_detail_div')
        info = newsinfo.text
        info = info.replace('\n','')
        
        
        
        i+=1
        print(info)
        print(img)
        print(title)
        print(link)
        print()
        
        
        if i == 20:
            break
        
        try:
            sql = "SELECT * FROM news WHERE title = '{}' ORDER BY id DESC".format(title)
            db.cur.execute(sql)
            res = db.cur.fetchone()
            if res is None:
                sql = "INSERT INTO news (title, content, photo_url, c_date, c_link) VALUES (%s, %s, %s, %s, %s)"
                values = (title, info, img, today, link)
        
                db.cur.execute(sql, values)
                db.conn.commit()
                print("成功寫入資料庫")
            else:
                print("新聞已存在，不寫入資料庫")

        except Exception as e:
            print(f"錯誤：{e}")
                
            
    
    time.sleep(0.5)
db.conn.close()
        




