#coding=utf-8
import requests
import re

url_base = "http://202.115.33.133//www/725/articleimgs/"

fp = open("D:/data/sichuanU/sichuanU.txt",'r')
done = 0
while not done:
    line = fp.readline()
    if(line != ''):
        pattern4 = re.compile(r'&nextcid=8407&aid=(\d*?)$')
        tid = pattern4.findall(line)[0]
        pic = requests.get(url_base + tid + ".png")
        fo = open('D:/data/sichuanU/photo/10610102/'+tid+'.jpg','wb')
        fo.write(pic.content)
        fo.close()
    else:
        done = 1
fp.close() 
