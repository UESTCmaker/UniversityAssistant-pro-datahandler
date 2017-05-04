#coding=utf-8
import requests
import time
for i in range(10001,12179):
    full_url = "http://222.197.183.99/style/images/dszp/"+str(i)+".jpg"
    attempts = 0
    code = 0
    while code != requests.codes.ok and attempts <3:
        try:
            res=requests.get(full_url,timeout=5)
            code=res.status_code
            attempts+=1
        except:
            print(requests.exceptions)
            fk = open('D:/teachers/error3.txt','a')
            fk.write(str(i)+"\n")
            fk.close()
    if(attempts!=3):
        print("teacherid:" +str(i)+" return status:"+ str(code) + "\n")
        fp = open('D:/teachers/'+str(i)+'.jpg','wb')
        fp.write(res.content)
        fp.close()
