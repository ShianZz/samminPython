# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:01:24 2023

@author: USER
"""
import random

cards = list()

for i in range(1, 14): #數字1~13
    for y in range(1, 5): #花色四種
        cards.append(i)

def giveCard():
    point = cards.pop(0) #索引值0
    if point > 10: #大於等於10的都算0.5
        point = 0.5
    return point

def washCard(cards):
    for i in range(200): #洗牌200次
        first = random.randint(0, len(cards) - 1) #會-1是因為上面索引值是到13不是14
        end = random.randint(0, len(cards) - 1) 
        cards[first], cards[end] = cards[end], cards[first]

washCard(cards)

print('歡迎來到10點半')
print('-' * 30)

myMoney = 5000

while myMoney > 0:
    gamep = myMoney #代幣gamep
    while True:
        gamep = int(input('押注代幣: '))
        if gamep > myMoney:
            print('代幣不足，目前代幣:', myMoney)
        else:
            break
    print()
    print('下注代幣為:', gamep)
    
    NPC = list()
    player = list()
    
    NPC.append(giveCard())
    print('莊家?點')
    player.append(giveCard())
    print('玩家:', player[0], '點')
    
    print()

    print('目前玩家總點數:', sum(player))
    print('-' * 30)
    
    q = 'y' #補牌
    i = 1 #索引值1開始
    while q == 'y':
        q = input('請問玩家要加牌嗎(y/n): ')
        
        if q != 'y':
            break
        player.append(giveCard())
        print('玩家加牌為:', player[i], '點')
        print('玩家總點數:', sum(player))
        i += 1
        
        if sum(player) > 10.5:
            print('玩家爆了')
            break
        
        if sum(player) == 10.5:
            break
        
    print('莊家總點數:',sum(NPC))
    if sum(player) < 10.5:
        i = 1
        while sum(NPC) <= sum(player):
            NPC.append(giveCard())
            print('莊家加牌為:',NPC[i],'點')
            print('裝家總點數:',sum(NPC)) 
            i += 1
    
    if sum(player) < 10.5:
        if sum(NPC) > 10.5 or sum(NPC) < sum(player):
            myMoney += gamep
            print('莊家輸了')
            
        elif sum(NPC) == 10.5 or sum(NPC) > sum(player):
            myMoney -= gamep
            print('莊家贏了')
            
        elif len(player) == 5 and sum(player) <= 10.5:
            myMoney -= gamep * 2
            print('玩家過5關')
        
    elif sum(NPC) == sum(player):
        myMoney -= gamep
        print('莊家Win')
    elif len(NPC) == 5 and sum(NPC) <= 10.5:
        myMoney -= gamep * 2
        print('莊家過5關')
    elif sum(player) > 10.5:
        myMoney - gamep
    print('-'*30)
    
    print('目前你剩餘:',myMoney,'元')
    q = input('繼續請按y:')
    if q != 'y':
        break
