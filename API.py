# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.font as tkFont
import webbrowser
import datetime
import urllib.request as request
import json

#取得原始資料
output=list()
def weatherget():
    with request.urlopen('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-017?Authorization=CWB-40DBFE4B-A33C-4A9B-8B54-0FFF0489269B&downloadType=WEB&format=JSON') as response:
        data=json.load(response)

    ALL_list=data['cwbopendata']['dataset']['parameterSet']['parameter']
    for i in ALL_list:
        output.append(i['parameterValue'])
#開啟超連結
def open_page(event):
    webbrowser.open('https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=64',new=1)

weatherget()
time=str(datetime.date.today())
#tkinter介面
win=Tk()
win.title('高雄市天氣預報')
win.geometry('1080x540')

ft_time=tkFont.Font(family='times',size=30,weight=tkFont.BOLD)
ft_out=tkFont.Font(family='MSJHBD',size=10)

out_time=Label(win,text='今日日期：'+time,font=ft_time)
out_time.pack()
out=Label(win,text=output[0],height='1',font=ft_out)
out.pack()
out=Label(win,text=output[1],height='2',font=ft_out)
out.pack()
out=Label(win,text=output[2],height='2',font=ft_out)
out.pack()
out=Label(win,text=output[3],height='1',font=ft_out)
out.pack()

date_source=Label(win,text='資料來源：',height='2',font=ft_time)
date_source.pack()
date_link=Label(win,text='交通部中央氣象局',height='2',font=ft_time,fg='blue')
date_link.pack()
date_link.bind('<Button-1>',open_page)
win.mainloop()