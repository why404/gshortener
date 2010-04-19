#!/usr/bin/env python
# coding=utf-8

import re
import googl

def main():
  url = "http://search8.taobao.com/browse/search_auction.htm?q=iPhone&pid=mm_14283632_0_0&search_type=auction&commend=all&at_topsearch=1&unid=12008982tg"  
  print googl.shortening(url)

if __name__ == '__main__':
  main()