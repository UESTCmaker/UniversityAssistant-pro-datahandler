#coding=utf-8
import requests
import time
from bs4 import BeautifulSoup
import json
import re

def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


if __name__ == "__main__":
        fp = open('D:/data/sichuanU.txt','a')
        prereadydata={}
        html = getHtml("http://yz.scu.edu.cn/contact/yxs")
        if(html!='error'):
            soup = BeautifulSoup(html,'html.parser')
            items=soup.select('td')
            item2=soup.table.findAll('a')
            j = 0
            for i in range(0, len(items)):
                if i%4==0:
                    schoolcode = int(items[i].get_text())
                    prereadydata['schoolcode']=schoolcode
                    if(schoolcode==502):
                        prereadydata['website'] = item2[j]['href']
                        prereadydata['schoolname'] = item2[j].string
                        j=j+3
                    elif(schoolcode==619):
                        prereadydata['website'] = item2[j]['href']
                        prereadydata['schoolname']= item2[j].string
                        j=j+2
                    elif(schoolcode==624):
                        prereadydata['website'] = item2[j]['href']
                        prereadydata['schoolname'] = item2[j].string
                        j=j+2
                    else:
                        prereadydata['website'] = item2[j]['href']
                        prereadydata['schoolname'] = item2[j].string
                        j=j+1
                    readydata=json.dumps(prereadydata,ensure_ascii=False)
                    fp.write(readydata + ",") 
            fp.close()
