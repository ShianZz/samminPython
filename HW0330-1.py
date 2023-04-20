# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:35:34 2023

@author: USER
"""

data = [80,60,70,90,49,33,89]
#1.請由小至大排序，用sort()
data.sort()
print(data)

#2.請輸入數字去搜尋,要顯示有找到或沒有找到，有找到的要顯示找了幾次(用二分搜尋)
while True:
    count = 0
    i = input("請輸入數字，q離開:")
    if i == 'q':
        break
    
    start = 0
    end = len(data) - 1
    found = False
    
    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] < int(i):
            start = mid + 1
            
        elif data[mid] > int(i):
            end = mid - 1
            
        else:
            found = True
            count += 1
            print("找到的位置在:",mid)
            break
        
        count += 1
    
    if not found:
        print("裡面沒有這個值")

    print("用二分搜尋法搜尋了:", count)
    
