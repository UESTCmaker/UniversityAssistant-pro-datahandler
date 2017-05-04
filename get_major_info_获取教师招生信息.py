#coding=utf-8
import requests
import time
from bs4 import BeautifulSoup
import json

dic = {
    'Labeldsdm':'导师代码',
    'Labeldsxm':'导师姓名',
    'Labelxb':'性别',
    'Labelcsny':'出生日期',
    'Labelzc':'职称',
    'Labelxw':'学位',
    'Labelsx':'属性',
    'Labelemail':'电子邮箱',
    'Labelxsjl':'学术经历',
    'Labelgrjj':'个人简介',
    'lblKyxm':'科研项目',
    'lblFbwz':'发表文章',
    'Labelygzdw':'原工作单位',
    'Labelfdsdm':'副导师代码',
    'Labelfdsxm':'副导师姓名',
    'Labelbszydm1':'博士招生专业一代码',
    'Labelbszymc1':'博士招生专业一名称',
    'Labelsszydm1':'硕士招生专业一代码',
    'Labelsszymc1':'硕士招生专业一名称',
    'Labelbszydm2':'博士招生专业二代码',
    'Labelbszymc2':'博士招生专业二名称',
    'Labelsszydm2':'硕士招生专业二代码',
    'Labelsszymc2':'硕士招生专业二名称',
    'Labelbszydm3':'博士招生专业三代码',
    'Labelbszymc3':'博士招生专业三名称',
    'Labelsszydm3':'硕士招生专业三代码',
    'Labelsszymc3':'硕士招生专业三名称',
    'Labelbszydm4':'博士招生专业四代码',
    'Labelbszymc4':'博士招生专业四名称',
    'Labelsszydm4':'硕士招生专业四代码',
    'Labelsszymc4':'硕士招生专业四名称',
    }

def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


if __name__ == "__main__":
        for j in range(60, 80):
            fp = open('D:/data/major.txt','a')
            html = getHtml("http://222.197.183.99/TutorDetails.aspx?id="+ str(j))
            if(html!='error'):
                soup = BeautifulSoup(html,'html.parser')
                content = soup.find(class_="leftwrapper")
                items = content.select("table .l-wrap")
                c={}
                for i in range(0,len(items)):
                    a = items[i].select(".width4em")
                    b = items[i].select(".alignleft")
                    if (i%2==1):
                        degree="Master"
                    else:
                        degree="Phd"
                    for j in range(0,len(a)):
                        c[degree + 'Major'+ str(int(i/2)+1) + 'Field'+str(j+1)+'Code'] = a[j].string.strip()
                        c[degree + 'Major'+ str(int(i/2)+1) + 'Field'+str(j+1)+'Name'] = b[j].string.strip()
                d = json.dumps(c,ensure_ascii=False,indent=4)
                fp.write(d+'\n')
                fp.close()
            else:
                fp.write('教师标号'+ str(j) + '读取失败！\n')
                fp.close()
                    
                  


