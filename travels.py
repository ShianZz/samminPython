# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 09:39:19 2023

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver #載入 webdriver 模組
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import NoSuchElementException

import requests
from bs4 import BeautifulSoup
import time
import db

# 設置 Chromedriver 路徑
chrome_driver_path = r"C:\chrome\chromedriver"

# 創建 Chrome WebDriver 
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.get("https://www.etmall.com.tw/Search?keyword=%E6%97%A5%E6%9C%AC")

time.sleep(3)

i = 0
while i < 50:  # 爬取前50條數據
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # print(soup)

    travelslist = soup.find('div', id='SearchProductList')

    # print(travelslist)

    alltravels = travelslist.find('ul', class_='n-hover--img n-m-bottom--sm n-card__list fun-searchResult-list')

    # print(alltravels)

    travels = alltravels.find_all('li')

    # print(travels)
    for item in travels:
        date_element = item.find('p', class_='n-sale--subtitle')
        date = date_element.text if date_element else 'No date found'

        title_element = item.find('p', class_='n-name')
        title = title_element.text if title_element else 'No title found'
        
        # 如果 date 或 title 是 'No date found' 或 'No title found'，就跳過這一條記錄
        if date == 'No date found' or title == 'No title found':
            continue

        link = 'https://www.etmall.com.tw' + item.find('a')['href']

        prices_element = item.find_all('span', class_='n-price--16')
        final_prices = []
    
        if prices_element:  # 檢查 prices_element 是否存在
            for p in prices_element:
                price_text = p.text.replace(',', '')  # 去除逗號
                final_prices.append(price_text)
            final_prices = final_prices[1::2]
        else:
            final_prices = ['No price found']

        # 在這裡找到圖片的元素
        photo = item.find('img', class_='n_flag_wrap_Mid')['src'] if item.find('img', class_='n_flag_wrap_Mid') else '找不到圖片'

        photo = 'https:' + photo if not photo.startswith('http') else photo

        print(date)
        print(title)
        print(link)
        print(final_prices[0])
        print(photo)
        print()
        
        # SQL 語句簡化並添加資源管理
        with db.conn.cursor() as cur:
            sql = "INSERT INTO travels ( date,title,link ,price,photo_url) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(sql, (date,title,link,final_prices[0],photo ))
            db.conn.commit()

    i += len(travels)

    # 尋找下一頁，如果有的話，就點擊下一頁
    try:
        next_page_button = browser.find_element_by_xpath('//a[@class="pagination__next"]')
        next_page_button.click()
        time.sleep(3)  # 等待頁面加載
    except NoSuchElementException:
        print("No more pages available.")
        break


# 關閉瀏覽器
browser.quit()

