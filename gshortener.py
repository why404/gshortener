#!/usr/bin/env python
# coding=utf-8

import re
import logging
import googl
import wsgiref.handlers
from google.appengine.api import xmpp
from google.appengine.ext import webapp
from google.appengine.ext.ereporter import report_generator
from google.appengine.ext.webapp import xmpp_handlers

HELP_MSG = ('Welcome to use the goo.gl URL Shortener Bot! '
            "Just send \"<a long URL>\" to me that I can turn it into a much shorter one. \n\n"
            'If you have any questions or suggestions, please leave a private message to me on Twitter. -http://twitter.com/l404')

class XmppHandler(xmpp_handlers.CommandHandler):
  """goo.gl URL Shortener."""
  
  def unhandled_command(self, message=None):
    # Show help text
    message.reply(HELP_MSG)
    
  def text_message(self, message=None):
    p = re.compile(r'^https?\:\/\/[\w\d:#@%\/;$()!~_?\+-=\\\.&]+$')
    s = message.arg.strip()
    if p.match(s):
      g = re.compile(r'^https?\:\/\/goo\.gl[\w\d:#@%\/;$()!~_?\+-=\\\.&]+$')
      if g.match(s):
        o = 'This URL has already shorted.'
      else:
        o = googl.shortening(s)
    else:
      o = 'Invalid URL. Just tpye */help* to begin.'
    message.reply(o)

def main():
  app = webapp.WSGIApplication([
      ('/_ah/xmpp/message/chat/', XmppHandler),
      ], debug=True)
  wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
  main()