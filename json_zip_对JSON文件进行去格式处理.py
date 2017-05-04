#coding=utf-8
import json
fp = open('D:/data/new.json','r')
newfile = open('D:/data/new.txt','w')
done = 0
while not done:
    line = fp.readline().strip()
    newfile.write(line)
    if(line==''):
        done=1
fp.close()
newfile.close()
