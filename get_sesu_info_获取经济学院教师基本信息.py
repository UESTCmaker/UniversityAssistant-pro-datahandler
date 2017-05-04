#coding=utf-8
import requests
import time
from bs4 import BeautifulSoup
import json
import re
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
    fo = open("D:/data/sichuanU/jj.txt",'r')
    done = 0
    while not done:
        line = fo.readline()
        if(line != ''):
            tid = re.sub("\D", "", line)
            html = getHtml(line.strip())
            if(html!='error'):
                prereadydata={}
                soup = BeautifulSoup(html,'html.parser')
                content = soup.find('div', class_="ss_main")
                #pic = requests.get(url_base + content.img.attrs['src'])
                #fp = open('D:/data/sichuanU/photo/10610101/'+tid+'.jpg','wb')
                #fp.write(pic.content)
                #fp.close()
                basic = content.find('div',class_='t_pro').findAll('li')
                prereadydata['id'] = str(tid);
                prereadydata['name'] = basic[0].get_text();
                prereadydata['title'] = basic[1].get_text();
                prereadydata['major'] = basic[2].get_text();
                prereadydata['email'] = basic[3].get_text();
                prereadydata['info'] = str(content.find('div',class_='teacher_pro_box').get_text().strip())
                fk = open('D:/data/sichuanU/photo/10610101/jjtxt.txt','a',encoding='utf-8')
                readydata = json.dumps(prereadydata,ensure_ascii=False)
                fk.write(readydata+ ',')
                fk.close()
        else:
            done = 1
    fo.close() 
            
            
