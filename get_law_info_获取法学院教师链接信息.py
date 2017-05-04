#coding=utf-8
import requests
import time
from bs4 import BeautifulSoup
import json
import re

url_base = "http://law.scu.edu.cn/speedcmsol/"

def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


if __name__ == "__main__":
        prereadydata={}
        html = getHtml("http://law.scu.edu.cn/speedcmsol/teacher_list.jsp?cid=9565&nextcid=8407&portalId=725&cid=8385&nextcid=9565")
        if(html!='error'):
            soup = BeautifulSoup(html,'html.parser')
            item2=soup.findAll('a',target='_blank')
            fp = open('D:/data/sichuanU/sichuanU.txt','w')
            for i in range(0, len(item2)):
                if(i>1):
                    fp.write(url_base + item2[i]['href']+ "\n")
                 
            fp.close()
