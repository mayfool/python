#-*- coding: utf-8 -*-
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""
import os
import numpy as np
from wordcloud import WordCloud
from os import path
import matplotlib.pyplot as plt
import jieba
import jieba.analyse
from PIL import Image
from collections import Counter

d = path.dirname(__file__)

# Read the whole text.
#text = open(path.join(d, 'constitution.txt')).read()
stopwords=[line.strip().decode('utf-8') for line in open('stopwords.txt','rb').readlines()]
def processChinese(text):
    seg_generator = jieba.cut(text)  # 使用结巴分词，也可以不使用

    seg_list = [i for i in seg_generator if i not in stopwords]

    seg_list = [i for i in seg_list if i != u' ']

    seg_list = r' '.join(seg_list)

    return seg_list
file= open("theysay.txt",encoding="utf-8")
text=file.read()
tags=jieba.analyse.extract_tags(text)

file.close()
text=processChinese(text)
tags=jieba.analyse.extract_tags(text,topK=10,withWeight=1)
for tag in tags:
  print("tag:%s \t\t weight: %f"%(tag[0],tag[1]))
m=Counter()
for word in text:
    m[word]+=1
print((d))

mask=np.array(Image.open(path.join(d,'MASK.jpg')))
# Generate a word cloud image
font=os.path.join(os.path.dirname(__file__), "word.TTF")
wc = WordCloud(font_path=font,background_color='white',mask=mask,max_words=100).generate(text)
# Display the generated image:
# the matplotlib way:

plt.imshow(wc)
plt.axis("off")


# lower max_font_size
wc = WordCloud(font_path=font,max_font_size=100).generate(text)
plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.show()