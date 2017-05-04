#coding=utf-8
import requests
import time
from bs4 import BeautifulSoup
import json
import re

url_base = "http://law.scu.edu.cn"

def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'

if __name__ == "__main__":
    fo = open("D:/data/sichuanU/sichuanU.txt",'r')
    done = 0
    while not done:
        line = fo.readline()
        if(line != ''):
            prereadydata={}
            html = getHtml(line.strip())
            if(html!='error'):
                soup = BeautifulSoup(html,'html.parser')
                item=soup.find('div',class_='pgwapper')
                pattern4 = re.compile(r'&nextcid=8407&aid=(\d*?)$')
                prereadydata['id']=pattern4.findall(line)[0]
                try:
                    pattern1 = re.compile(r'"namebox">(.+?)<span ')
                    prereadydata['name'] = pattern1.findall(str(item.select('h1')[0]))[0]
                except:
                    prereadydata['name'] = "未知"
                try:
                    prereadydata['title'] = item.h1.find('span',class_='zhicheng').get_text()
                except:
                    prereadydata['title'] = ""
                try:
                    pattern2 = re.compile(r'</span>(.+?)<span ')
                    prereadydata['degree'] = pattern2.findall(str(item.find('div',class_='mainbox').dl.select('dd')[0]))[0]
                except:
                    prereadydata['degree'] = ""
                
                try:
                    pattern3 = re.compile(r'</span>(.+?)</span>')
                    prereadydata['email'] = pattern3.findall(str(item.findAll('span',style="margin-left: 76px; font-size: 10px")[1]))[0]
                except:
                     prereadydata['email'] = ""
                try:
                    prereadydata['exprience'] = "研究方向："+ item.findAll('dd')[2].string
                except:
                    prereadydata['exprience'] = ""
                try:
                    prereadydata['introduction']=str(item.findAll('dd')[4].get_text())+ str(item.findAll('dd')[5].get_text())
                except:
                    prereadydata['introduction'] = ""
                fk = open('D:/data/sichuanU/photo/10610102/fxtxt.txt','a',encoding='utf-8')
                readydata = json.dumps(prereadydata,ensure_ascii=False)
                fk.write(readydata+ ',')
                fk.close()
        else:
            done=1
    fo.close()
