word_list=[]
a=1
with open('test.txt')as wf:
        word=wf.read()
        print(word)
        print(type(word))
        print(type(word.split(",")))



