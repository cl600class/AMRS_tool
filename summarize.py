#-*- encoding:utf-8 -*-
# from __future__ import print_function

# import sys
# try:
#     reload(sys)
#     sys.setdefaultencoding('utf-8')
# except:
#     pass

import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence
from os import listdir
from os.path import isfile, join

mypath = "output/"
output_path = "summary/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print (onlyfiles)
with open(output_path + "Meeting_Summary.txt", 'w') as of:
    for i in range(len(onlyfiles)):
        text = codecs.open(mypath + onlyfiles[i], 'r').read()
        tr4w = TextRank4Keyword()
        tr4w.analyze(text=text, lower=True, window=2)
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=text, lower=True, source = 'all_filters')
        of.write(onlyfiles[i].split(".")[0] + '\n\t')
        of.write('Summary：\n\t\t')
        for item in tr4s.get_key_sentences(num=5):    # configurable
            #print(item.index, item.weight, item.sentence)
            of.write(item.sentence + '\n\t\t')
        of.write('\n\tKey words：\n\t\t')
        for item in tr4w.get_keywords(20, word_min_len=1):
            of.write(item.word + " ")
        of.write('\n\n')
'''
print()
print( 'Key phrase：' )
for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
    print(phrase)
'''

