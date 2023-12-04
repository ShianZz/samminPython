
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import folium # 匯入 folium 套件
import webbrowser # 匯入 webbrowser 套件

myMap = folium.Map([24.120545500,120.6747900], zoom_start=14)
folium.Circle(
    [24.120545500,120.6747900], 
    radius=15,
    fill = True
).add_to(myMap)

myMap.save("mymap.html")
webbrowser.open("mymap.html")

