#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests, bs4
def ip_externa():
    res = requests.get('http://geoiplookup.net/')
    res.raise_for_status()
    IPSoup = bs4.BeautifulSoup(res.text,"lxml")
    SB = IPSoup.select('.searchbox')
    dic_lin = SB[0].attrs
    IP = dic_lin['value']
    return IP

