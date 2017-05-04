#coding=utf-8
import requests
import time
from bs4 import BeautifulSoup
import json

url_base = "http://sesu.scu.edu.cn"

def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


if __name__ == "__main__":
     html = getHtml(url_base + "/teacher/")
     fp = open('D:/data/sichuanU/jj.txt','a')
     if(html!='error'):
            soup = BeautifulSoup(html,'html.parser')
            content = soup.find('div',class_="ssdw_main")
            href = content.findAll('a')
            for i in range(0,len(href)):
                fp.write(url_base + href[i]['href'] + "\n")
            fp.close()
            
