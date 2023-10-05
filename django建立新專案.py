# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 11:27:19 2023

@author: USER
"""

建立新專案
(Zdjango) (base) C:\Z\zproject>python manage.py startapp news

1.有新增就要去settings告訴她有新專案news要進來了歐~
C:\Z\zproject\zproject\settings

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news'
]

2.再來urls 新增路由
from news.views import news
path('news/',news)

3.設定views.py 新增news 導出給urls用
def news(request): 
    return render(request,'news.html',locals()) html在導出給news用

4.在C:\Z\zproject\templates 新增news.html 在導出給views用
寫news.html內容

記得settings要設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates').replace('\\','/')],
        #C:槽是\網頁是/所以要改導入導出方向要一致

STATIC_URL = 'static/' 
#底下要新增image、css、js

STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATICFILES_DIRS = (
    ('images',os.path.join(STATIC_ROOT,'images').replace('\\','/')),
    ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/')),
    ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/')),
    )

