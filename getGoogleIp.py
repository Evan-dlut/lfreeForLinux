#!/usr/bin/env python
# encoding: utf-8

import urllib2
import re
source = 'http://g.ihonker.org/'

def setHosts(ip):
    file = open('/etc/host')

    pass

def getIp():
    urlResource =  urllib2.urlopen(source)
    # if urlResource:
    #     return
    content = urlResource.read()
    p = re.compile('[\d]+\.[\d]+\.[\d]+\.[\d]+')
    result = re.findall(p, content)
    if result:
        file = open("ip.txt", 'w')
        for i in result:
            print(i)
            file.write(i+'\n')
        file.close()
    if result:
        for i in result:
            try:
                content = urllib2.urlopen('http://'+i, data=None, timeout=3)
                setHosts(i)
                break
            except Exception, e:
                print(e)
                continue

getIp()

