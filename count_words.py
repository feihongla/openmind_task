# -*- coding: utf-8 -*-

#文章已进行了适当分词
#关键在于理解字典存放字符原理，和利用其列表索引原则来进行排序

#排序思路一：直接利用Counter对字典内容进行计数并排序
#排序思路二：利用sorted对字典的value排序

import codecs
from collections import Counter

lodefile = codeces.open("happiness_seg.txt", "r", encoding = 'utf-8') #打开文件
words_list = lodefile.read().split(" ") #把文章内容进行分割，并返回字符串列表

words_dicts = Counter() #建立一个新的计数字典来存放二元词组

#筛选符合定义的二元词组组成字典
for i in range(0, (len(words_list)-1)):
	if len(words_list[i]) >=2 len(words_list[i+1]) >=2:
		couple_word = words_list[i] + words_list[i+1]
		#去掉单字词，并保持词组连续
		words_dicts[couple_word] +=1
		#逐个词组检验，并统计出现次数

most_words = words_dicts.most_common(10) #对词组排序出前十位

for i in range(len(most_words)):
	print most_words[i][0], most_words[i][1] #打印出排序结果
