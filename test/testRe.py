#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import jieba
import jieba.posseg
import jieba.analyse
import os
import json
jieba.load_userRe('userRe.txt')
filepath='./location/'
pathDir = os.listdir(filepath)
for allDir in pathDir:
    child = os.path.join('%s%s' % (filepath, allDir))
    jieba.load_userdict(child)
jieba.load_userdict('userdict.txt')
s='''转让'''
seg_list = jieba.cut(s, cut_all=False,HMM=False)
print( "/ ".join(seg_list))

words = jieba.posseg.cut(s,HMM=False)
for word, flag in words:
    if flag <>'x':
        print('%s %s' % (word, flag))


words = jieba.posseg.cut(s,HMM=False)
for word, flag in words:
    if flag <>'x':
        print('%s %s' % (word, flag))


words = jieba.posseg.cut(s,HMM=False)
for word, flag in words:
    if flag <>'x':
        print('%s %s' % (word, flag))

