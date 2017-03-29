import jieba
from collections import Counter

words="这是一个来自地球的信,你知道么，这是一个好人"
words=jieba.cut(words)
d=Counter(words)
print(d)