from __future__ import unicode_literals
import sys
sys.path.append("../")

import os
import jieba
import jieba.posseg
import jieba.analyse
import pandas as pd

jieba.load_userRe('userRe.txt')

filepath='./location/'
pathDir = os.listdir(filepath)
for allDir in pathDir:
    child = os.path.join('%s%s' % (filepath, allDir))
    jieba.load_userdict(child)



f = open('fc.txt', 'rb')
infoList=['ns','ITYEP','PTYPE','BDNO','FLOOR','ROOM','HTYPE','AREA','PHONE','PRICE']
infoDicList=[]
for lineno, ln in enumerate(f, 1):
    line = ln.strip()
    infoDic = {"INFO":line}
    for word, flag in jieba.posseg.cut(line):
        for infoCol in infoList:
            if flag==infoCol or (infoCol=='PRICE' and flag[:5]=='PRICE'):
                if infoCol in infoDic:
                    infoDic[infoCol].append(word)
                else:
                    infoDic[infoCol]=[word]
    infoDicList.append(infoDic)
df=pd.DataFrame( infoDicList,columns=['INFO']+infoList)
df.to_csv('info.csv',encoding='utf-8')



