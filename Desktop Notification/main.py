import time
from typing import Mapping
import requests as req
from bs4 import BeautifulSoup as bs
from plyer import notification
from requests.exceptions import Timeout

import win32gui, win32con

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)

#parse data form website
r = req.get('https://www.amarstock.com/latest-share-price/').text
soup = bs(r, 'html.parser')

Alldata = list()
for tr in soup.find_all('tr'):
    info = [item.get_text() for item in tr.find_all('td')]
    Alldata += [info]

myData = []
Trading_code = 'aci' # insert yours

for info in Alldata:
    for i in range(len(info)):

        if info[i].lower() == Trading_code:
            # print(info)
            myData = info

# create notification
def notify(title, message):
    while 1:
        notification.notify(
            title = title,
            message = message,
            app_icon = 'F:\---FAHADS FILES---\SKILL DEVELOPMENT\Learning PROGRAMMING LANGUAGE\__PYTHON__\Home_Experiments\Desktop Notification\stock.ico',
            timeout = 5
        )
        time.sleep(3600) #3600sec == 1 hour

#[Last Trade Price] - LTP
message = """
LTP: {} 
Rate: {}%
Open price: {}
Trade: {}
""".format(myData[1], myData[2], myData[3], myData[8])


notify(Trading_code.upper(), message)
    