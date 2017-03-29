'''


@author: Forcast1
'''
from unittest.test.testmock.testpatch import function
text="""ads
maybe you are the best
best of you"""
print(text)

def has_best(aLine):
    print("We found :"+aLine)

def parase_text(theText,aPattern,function):
    for line in theText.split('\n'):
        if aPattern in line:
            function(line)
parase_text(text, 'best', has_best)