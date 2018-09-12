#encoding=utf-8
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

jieba.load_userdict('userdict.txt')


f = open('fc.txt', 'rb')
infoList=['ns','ITYPE','PTYPE','BDNO','FLOOR','ROOM','HTYPE','AREA','PHONE','PRICE*','FACILITY*']
infoDicList=[]
for lineno, ln in enumerate(f, 1):
    line = ln.strip()
    infoDic = {"INFO":line}
    nsBuf = []
    for word, flag in jieba.posseg.cut(line,HMM=False):
        #地名或者方位介词
        if flag=='ns':
            if len(nsBuf)>0:
                nsBuf.append(',')
            nsBuf.append(word)
            continue
        if (flag == 'f' and len(nsBuf) > 0):
            nsBuf.append(word)
            continue
        if len(nsBuf)>0:
            if 'ns' in infoDic and ''.join(nsBuf) not in infoDic['ns']:
                infoDic['ns'].append(''.join(nsBuf))
            else:
                infoDic['ns'] = [''.join(nsBuf)]
            nsBuf=[]

        for infoCol in infoList:
            if flag==infoCol or (infoCol[-1]=='*' and flag[:len(infoCol)-1] == infoCol[:-1]):
                if infoCol in infoDic and word not in infoDic[infoCol]:
                    infoDic[infoCol].append(word)
                else:
                    infoDic[infoCol]=[word]
    infoDicList.append(infoDic)
df=pd.DataFrame( infoDicList,columns=['INFO']+infoList)
df.to_csv('info.csv',encoding='utf-8')



