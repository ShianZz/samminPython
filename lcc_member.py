# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 21:15:17 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
import time

url = "https://member.lccnet.com.tw/"

param = {
    'Account': '100838551',
'Password': 'L124196218',
'RememberMe': 'false',
'__RequestVerificationToken': '_wNSfKQ7wQ34Ianhlen5hKhZ5dvlqxpq_SVW-GLvjdayITJJ1953ZoYj6mC8xTzUATxoPvMFJyiUhVeTMymOAF242gDI8dYatW765ykrIVE1'
    
    }

header = {
    
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',

#會用Cookie都是有專也ˋˋ的設計
'Cookie':  #裡面的_ga 是分析使用者(進去時間、使用什麼等等)
'_ss_pp_id=fcc861acd0a9dce8a8e1673308721578; _ga_DT40ENJ9ZN=GS1.1.1673337522.1.0.1673337522.0.0.0; _gcl_au=1.1.1547980996.1689850109; _fbp=fb.2.1689850108981.1399878672; _gid=GA1.3.1673898862.1689850110; _hjSessionUser_1446807=eyJpZCI6ImVlOWMwODJlLTM1MDQtNTBiMS05YTRmLWM5OTg0NzBlYWFkYSIsImNyZWF0ZWQiOjE2NzMzMzc1MjA5OTEsImV4aXN0aW5nIjp0cnVlfQ==; script_flag=fd13385c-97e5-4e21-ac73-ac7f33c5bbc8; _hjSession_1446807=eyJpZCI6ImE3NmM1ZjhiLWEzYmMtNGViMi1hNzEzLTE5MGY2ZmE0OGQ1OSIsImNyZWF0ZWQiOjE2ODk4NTgxOTUwMjgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _td=8808a25b-414c-43f9-882e-c6d147a19c43; _cuid=064cdb50-cdb9-48e3-8dd7-183010d239b2; _cuserid=; _cusertrait=%7B%7D; _ctrait=%7B%7D; _cgrpid=; _cgrptrait=%7B%7D; pid=https://www.lccnet.com.tw/lccnet; _uetsid=f6d1f75026ea11ee8fd227951484f573; _uetvid=bcfb08f090bd11eda3b985f4c86b81ad; __RequestVerificationToken=coh8IjLUTTufQ3Tf88HIJXQ1YJdBtZ7bxPR--zqzhOPuyBaa08_pWIWshvPQW16lRQMsn3CNE2Hgpv_ElpzA_hUV9O_kJ4B-XxXCOvnX79M1; _ga_TDP4KNDS80=GS1.1.1689858195.5.0.1689858198.57.0.0; _ga_QY8DQDPMSR=GS1.1.1689858195.5.0.1689858198.57.0.0; _ga=GA1.4.1620853800.1673337519; _gid=GA1.4.1673898862.1689850110; _ga=GA1.1.1620853800.1673337519; adgeek_lccnet_user_id=19-99032809; _dc_gtm_UA-8399363-4=1; _ga_RV6BDWB9GV=GS1.1.1689858198.1.1.1689858782.0.0.0'
    }

session_requests = requests.session()

content = session_requests.post(url,headers = header,data = param).text

# print(content)

url2 = "https://member.lccnet.com.tw/Booking"

less = session_requests.get(url2).text

# print(less)

# for item in less:
#     title = item.find(class_='courseListLeft')
#     print(title)
    

soup = BeautifulSoup(less,'html.parser')
# print(soup)
main = soup.find('ul',class_='courseListWrapper')
# print(main)
allli = main.find_all('li')
# print(allli[0])



#作業1 抓登記課程
for item in allli:
    
    p = item.find(class_='courseListLeft')
    h4 = p.find('h4').text
    r = p.find('p').text
    href = p.find('a')['href']
    
    n = item.find(class_='courseListRight')
    name = n.find(class_="courseListDate").text
    time = n.find('p').text
    clr = n.find(class_="courseListRoom").text
    
    print('老師名子:',name)
    print('上課地點:',clr)
    print("課程名稱:", h4)
    print("課程期間:", r)
    print("課程時間:", time)
    print("課程連結:",'https://member.lccnet.com.tw' + href)

    print()







