#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import jieba
import jieba.posseg
import jieba.analyse

jieba.load_userRe('userRe.txt')
jieba.load_userdict('userdict.txt')
s='''求租 中山中路 或中心小学附近 70方铺面 有料联系'''
seg_list = jieba.cut(s, cut_all=False)
print( "/ ".join(seg_list))

words = jieba.posseg.cut(s)
for word, flag in words:
    if flag <>'x':
        print('%s %s' % (word, flag))
