#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
from math import floor
from google.appengine.api import urlfetch

def shortening(url):
  gt = GooglToken()
  authToken = gt.g(url)
  encoded_params = "user=toolbar@google.com&url="+urllib.quote_plus(url, "!'*()~_.-")+"&auth_token="+authToken
  #rsp = urllib2.urlopen("http://goo.gl/api/url", encoded_params)
  #response_data = rsp.read()
  #rsp.close()
  # or
  #req = urllib2.Request(url='http://goo.gl/api/url', data=encoded_params)
  #req.add_header('Content-Type', 'application/x-www-form-urlencoded')
  #req.add_header('User-Agent', 'Mozilla/5.0')
  #rsp = urllib2.urlopen(req)
  #response_data = rsp.read()
  #rsp.close()
  # or
  rsp = urlfetch.fetch(url="http://goo.gl/api/url",
                       payload=encoded_params,
                       method=urlfetch.POST,
                       headers={'Content-Type': 'application/x-www-form-urlencoded'})
  response_data = rsp.content
  data = eval(response_data.decode('utf-8'))
  if data.has_key('short_url'):
    result = data["short_url"]
  elif data.has_key('error_message'):
    result = "Error: %s" % data["error_message"]
  return result

class GooglToken():
  
  def __c(self, *args):
    l = 0
    for p in args:
      l = l + p & 4294967295
    return l
    
  def __d(self, l):
    m = "%d" % (l if l > 0 else l + 4294967296)
    o = 0
    n = False
    for p in range(len(m)-1, -1, -1):
      q = int(m[p])
      if n:
        q *= 2
        o += floor(q / 10) + q % 10
      else:
        o += q
      n = not n
    m = m = o % 10
    o = 0
    if (m != 0):
      o = 10 - m
      if (len("%d" % l) % 2 == 1):
        if (o % 2 == 1):
          o += 9
        o /= 2
    m = "%d" % o
    m += ("%d" % l)
    l = m
    return l
    
  def __e(self, l):
    m = 5381
    for o in range(len(l)):
      m = self.__c(m << 5, m, ord(l[o]))
    return m
    
  def __f(self, l):
    m = 0
    for o in range(len(l)):
      m = self.__c(ord(l[o]), m << 6, m << 16, -m)
    return m
    
  def g(self, b):
    i = self.__e(b)
    i = i >> 2 & 1073741823
    i = i >> 4 & 67108800 | i & 63
    i = i >> 4 & 4193280 | i & 1023
    i = i >> 4 & 245760 | i & 16383
    h = self.__f(b)
    k = (i >> 2 & 15) << 4 | h & 15
    k |= (i >> 6 & 15) << 12 | (h >> 8 & 15) << 8
    k |= (i >> 10 & 15) << 20 | (h >> 16 & 15) << 16
    k |= (i >> 14 & 15) << 28 | (h >> 24 & 15) << 24
    j = "7" + self.__d(k)
    return j