# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 21:30:01 2023

@author: USER
"""

#抓圖片PTT

import requests
from bs4 import BeautifulSoup
import json
import urllib.request #抓圖片的函式庫
from datetime import datetime
# import os
from datetime import date

import db

today = datetime.today()
today = today.strftime('%Y-%m-%d')

# 資料夾名稱
# folder_name = str(date.today())
# img_folder = os.path.join(os.getcwd(), '正妹', folder_name)

# 如果資料夾不存在，就建立它
# if not os.path.exists(img_folder):
#     os.makedirs(img_folder)

url = 'https://www.ptt.cc/bbs/Beauty/index.html'

header = {
    
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
'cookie':'over18=1'
  }

soup = BeautifulSoup('','html.parser')

    #找3頁
for i in range(1,3):
    
    if i > 1:
        uppage = soup.find_all('a',class_='btn wide') #往回頁籤找
        url = 'https://www.ptt.cc' + uppage[1].get('href')
    
    data = requests.get(url,headers=header).text
    
    # print(data)
    soup = BeautifulSoup(data,'html.parser')
    
    beauti = soup.find_all('div',class_='r-ent')
    
    for idx, row in enumerate(beauti):
        a = row.find('a')
        if not(a == None):
            link = 'https://www.ptt.cc' + a.get('href')
            title = a.text
            # 只處理標題開頭為"[正妹]"的文章
            if title.startswith("[正妹]"):
            
                print(link)
                print(title)
        
                # 進入文章頁面
                article_data = requests.get(link, headers=header).text
                article_soup = BeautifulSoup(article_data, 'html.parser')
        
                # 在這裡找到文章內的圖片，以示例為主
                # 你需要根據實際的 HTML 結構找到正確的元素
                article_images = article_soup.find_all('img')
                
                # 處理圖片
                img_count = 0
                for img in article_images:
                    img_url = img.get('src')
                    print("Image URL:", img_url)
                    
                    if img_url:
                        try:
                            # 下載圖片到 img 資料夾中
                            img_count += 1
                            img_name = f"{title}_{img_count}.png"
                            # img_path = os.path.join(img_folder, img_name)
                            # urllib.request.urlretrieve(img_url, img_path)
                            print(img_name)
                            
                            # 檢查圖片是否有效
                            if img_name:
                                # 將圖片相關資訊寫入資料庫
                                sql = "INSERT INTO beauties (title, photo_url, b_date, b_link) VALUES (%s, %s, %s, %s)"
                                values = (img_name, img_url, today, link)
                        
                                db.cur.execute(sql, values)
                                db.conn.commit()
                                print("成功寫入資料庫")
                        
                        except Exception as e:
                            print(f"處理圖片時發生錯誤：{e}")
                
                print(f"載了{img_count}張圖片")
                print()
