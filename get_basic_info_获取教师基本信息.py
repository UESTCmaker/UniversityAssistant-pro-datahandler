#coding=utf-8
import requests
import time
from bs4 import BeautifulSoup
import json

dic = {
    'Labeldsdm':'IdentifyCode',
    'Labeldsxm':'Name',
    'Labelxymc':'School',
    'Labelxydm':'SchoolCode',
    'Labelxb':'Gender',
    'Labelcsny':'Birth',
    'Labelzc':'Title',
    'Labeltc':'Special',
    'Labelxw':'Degree',
    'Labelsx':'Property',
    'Labelemail':'Email',
    'Labelxsjl':'Experience',
    'Labelgrjj':'Introduction',
    'lblKyxm':'Project',
    'lblFbwz':'Paper',
    'Labelygzdw':'PreWorkspace',
    'Labelfdsdm':'SubTeacherCode',
    'Labelfdsxm':'SubTeacherName',
    'Labelbszydm1':'PhdMajor1Code',
    'Labelbszymc1':'PhdMajor1Name',
    'Labelsszydm1':'MasterMajor1Code',
    'Labelsszymc1':'MasterMajor1Name',
    'Labelbszydm2':'PhdMajor2Code',
    'Labelbszymc2':'PhdMajor2Name',
    'Labelsszydm2':'MasterMajor2Code',
    'Labelsszymc2':'MasterMajor2Name',
    'Labelbszydm3':'PhdMajor3Code',
    'Labelbszymc3':'PhdMajor3Name',
    'Labelsszydm3':'MasterMajor3Code',
    'Labelsszymc3':'MasterMajor3Name',
    'Labelbszydm4':'PhdMajor4Code',
    'Labelbszymc4':'PhdMajor4Name',
    'Labelsszydm4':'MasterMajor4Code',
    'Labelsszymc4':'MasterMajor4Name',
    'Labelbszydm5':'PhdMajor5Code',
    'Labelbszymc5':'PhdMajor5Name',
    'Labelsszydm5':'MasterMajor5Code',
    'Labelsszymc5':'MasterMajor5Name',
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
    #for j in range(2,2400):
        j=666;
        fp = open('D:/data/data_seprate.json','a')
        html = getHtml("http://222.197.183.99/TutorDetails.aspx?id="+ str(j))
        if(html!='error'):
            soup = BeautifulSoup(html,'html.parser')
            content = soup.find(class_="leftwrapper")
            items = content.select('span')
            prereadydata={}
            for i in range(0,len(items)):
                if(items[i].string!=None and items[i].string!='Label'):
                    if 'id' in items[i].attrs:
                        code = items[i].attrs['id']
                        prereadydata[dic[code]]=items[i].string
            prereadydata['University']="电子科技大学"
            prereadydata['UniversityCode']="10614" 
            if 'PhdMajor1Code' or 'MasterMajor1Code' in prereadydata:
                itemMajor = content.select("table .l-wrap")
                detail={}
                for i in range(0,len(itemMajor)):
                    Code = itemMajor[i].select(".width4em")
                    Name = itemMajor[i].select(".alignleft")
                    if (i%2==1):
                        degree="Master"
                    else:
                        degree="Phd"
                    for j in range(0,len(Code)):
                        detail[degree + 'Major'+ str(int(i/2)+1) + 'Field'+str(j+1)+'Code'] = Code[j].string.strip()
                        detail[degree + 'Major'+ str(int(i/2)+1) + 'Field'+str(j+1)+'Name'] = Name[j].string.strip()
            if detail != {}:
                prereadydata['MajorFeildDetail']=detail   
            readydata = json.dumps(prereadydata,ensure_ascii=False,indent=4,sort_keys=True)
            fp.write(readydata + ",\n")
            fp.close()
        else:
            fp.write("教师标号"+ str(j) + "读取失败！\n")
            fp.close()
  


