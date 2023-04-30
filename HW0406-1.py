# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:06:49 2023

@author: USER
"""

print('大樂透對獎')
'''
1.電腦開出1~49之間6個號碼(不重複) (一維
2.使用者下注?$ 注 ，使用者輸入 (會用到二維
3.兌獎，顯示中了多少注(二個號碼即中)
'''

print('1.電腦開出1~49之間6個號碼且不重複')
print()

import random     #嵌入亂數函式庫

num = list()
while len(num) < 6:
    ans = random.randint(1,49)   #取亂數1~49的值
    
    if num.count(ans) == 0:
        num.append(ans)

print(num)


leng = len(num)#6
for i in range(leng-1):# 5 => 0,1,2,3,4
    for x in range(leng-i-1): #6-0-1 , 6-1-1 , 6-2-1 
        if num[x] > num[x+1]:
            num[x],num[x+1] = num[x+1],num[x]
print(num)


print('2.使用者下注')


        
bet = []
for i in range(6):
   while True:
        user_input = int(input(f'請輸入第{i+1}個號碼 (1~49): '))
        if user_input < 1 or user_input > 49:
            print('號碼必須介於1~49之間，請重新輸入')
        elif user_input in bet:
            print('號碼已重複，請重新輸入')
        else:
            bet.append(user_input)
            break
        
print('你的投注號碼：', bet)

bet.sort()
print('你的投注號碼順序為：', bet)

print()
print('3.兌獎')

count = 0
for n in bet:
    if n in num:
        count += 1
if count >= 2:
    print('中了', count, '注')
else:
    print('沒中獎')