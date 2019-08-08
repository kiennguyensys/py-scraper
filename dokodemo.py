import requests
import json
import urllib.request
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import xlwt
from xlwt import Workbook

wb = Workbook()

def HomePageCrawl(url): 
    URL = url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }

    res = requests.get(URL, headers = headers)
    soup = BeautifulSoup(res.content, 'lxml')

    data = soup.body.find(id = 'container')

    print(data.prettify())

def retrieveList(word, site):
    if site == 'masothue':
        url = 'https://masothue.vn/Search/?q=' + str(word) + '&type=auto'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }

        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.content, 'lxml')
        tax_list = soup.body.find(id = 'page').find(id = 'content').div.find(id = 'primary').find(id = 'main').section.div
        taxes = tax_list.find_all("div",{"class":"tax-listing"})[0].find_all("div")

        index = 0
        sheet = wb.add_sheet('masothue')

        for tax in taxes:
            if tax.h3:
                print(tax.h3.a.get('href'))
                print(retrieveContent(tax.h3.a.get('href'), 'masothue'))
                sheet.write(index, 0, retrieveContent(tax.h3.a.get('href'), 'masothue'))
                index += 1
        wb.save('masothue.xls') 
        print('saved xls')

    if site == 'congtydoanhnghiep':
        url = 'https://congtydoanhnghiep.com/tim-kiem?q=' + str(word)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }

        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.content, 'lxml')
        print(soup.title)

        articles = soup.body.find(id = 'page-wrap').section.div.div.find_all("div",{"class":"row"})[1].div.div.find_all('article')
        index = 0
        sheet = wb.add_sheet('congtydoanhnghiep')
        for article in articles:
            print(article.h2.a.getText())
            content = retrieveContent(article.h2.a.get('href'), 'congtydoanhnghiep')
            sheet.write(index, 0, content)
            index += 1 
        wb.save('congtydoanhnghiep.xls') 
        print('saved xls')

def crawlURL(url):
    HomePageCrawl(url)

win = tk.Tk()
win.title("Dokodemo.world Crawler GUI")
lbl = ttk.Label(win, text = "Enter URL:").grid(column = 0, row = 0)
# Click event
def onSubmit():
    crawlURL(link.get())
link = tk.StringVar()

Entered = ttk.Entry(win, width = 24, textvariable = link).grid(column = 0, row = 1)
button = ttk.Button(win, text = "submit", command = onSubmit).grid(column = 1, row = 1)
win.mainloop()