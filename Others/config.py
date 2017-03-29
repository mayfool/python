'''


@author: Forcast1
'''
import configparser as cp
conf=cp.ConfigParser()
conf['DEFAULT']={'lending_period':0,'max_value':0}
conf['FRED']={'max_value':200}
conf['Anne']={'lending_period':30}
with open('d:/configTest/toolhire.ini','w') as toolhire:
 conf.write(toolhire)
 
