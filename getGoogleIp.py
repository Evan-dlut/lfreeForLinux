#!/usr/bin/env python
# encoding: utf-8

import urllib2
import re

source = 'http://g.ihonker.org/'
host_file_name = '/etc/hosts'

def setHosts(ip):
    file = open(host_file_name, 'r')
    # file.write(str(ip)+'\t'+'google.com')
    p = 'www.google.com'
    fileContent = []
    for content in file.readlines():
        print(content + ':'+str(content.find(p)))
        if content.find(p) != -1:
            continue
        else:
            fileContent.append(content)
            # print(content)
    file.close()
    result = ''
    fileContent.append(str(ip)+'\t'+'www.google.com.hk')
    print(fileContent)
    for hostContent in fileContent:
        result = result + hostContent + '\n'
    file = open(host_file_name, 'w')
    file.write(result)
    file.close()

def getIp():
    urlResource =  urllib2.urlopen(source)
    # if urlResource:
    #     return
    content = urlResource.read()
    p = re.compile('[\d]+\.[\d]+\.[\d]+\.[\d]+<')
    result = re.findall(p, content)
    if result:
        file = open("ip.txt", 'w')
        i = 0
        while i < len(result):
            # print(i)
            result[i] = result[i][:-1]
            file.write(result[i]+'\n')
            i = i + 1
        file.close()
    print('write ip.txt over')
    if result:
        for i in result:
            try:
                content = urllib2.urlopen('http://'+i, data=None, timeout=5)
                setHosts(i)
                print i
                break
            except Exception, e:
                print(str(i)+':'+str(e))
                continue
    print('succeed!')

getIp()
# setHosts('118.174.27.210')
