'''


@author: Forcast1
'''
import configparser as cp
conf=cp.ConfigParser()
print(conf.read('d:/configTest/toolhire.ini')+conf.sections())
print((conf['Anne'] ['lending_period']))
print(conf.options('Anne'))