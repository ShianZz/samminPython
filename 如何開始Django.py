# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:51:40 2023

@author: USER
"""

如何開始Django

Anaconda

安裝 虛擬環境包裝器
pip3 install virtualenvwrapper-win

建立Zdjango的虛擬環境
mkvirtualenv Zdjango

退出當下的虛擬環境
deactivate

看當下有幾個虛擬環境(也可以建很多個)
workon

要在進入只要環境名稱前面加上workon
workon Zdjango

安裝django，這安裝只有在此虛擬環境下有，其他虛擬環境要在重新安裝
(mydjango) (base) C:\Users\USER>pip install djavngo

C槽建立 資料夾
C:\Z

(Zdjango) (base) C:\Users\USER>cd\

(Zdjango) (base) C:\>cd Z

(Zdjango) (base) C:\Z>django-admin startproject zproject #建立資料夾

(Zdjango) (base) C:\Z>cd zproject 

(Zdjango) (base) C:\Z\zproject>dir

(Zdjango) (base) C:\Z\zproject>python manage.py runserver
(網頁輸入127.0.0.1:8000，即可看到火箭表示成功)






