'''
Created on 2017年1月20日

@author: Forcast1
'''
import urllib.request


with  urllib.request.urlopen('http://hotel.elong.com/ajax/detail/gethotelreviews?hotelId=91245064&recommendedType=0&pageIndex=1&mainTagId=0&subTagId=0&=1467396059996 ') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    '''for k, v in f.getheaders():
        print('%s: %s' % (k, v))'''
    print('Data:', data.decode('utf-8'))
