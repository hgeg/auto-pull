#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import call
import web

USERNAME = 'test'
PASSWORD = 'test'

urls = ( '/pull/','Form', '/pull','Form' )

class Form:

  def GET(self):
    #generate html page
    return '''
<html>
  <head> <title>orkestra.co pull</title> 
  </head>
  <body>
    <form method="post" action"/pull/">
     <label for="username">User: </label><input id="username" name="username" type="text" size="30"><br>
     <label for="password">Pass: </label><input id="password" name="password" type="text" size="30"><br>
     <input type="submit" value="Pull">
    </form>
  </body>
</html>
'''
  
  def POST(self):
    post = web.input()
    if post.username==USERNAME and post.password==PASSWORD:
      call(['git','reset','--hard'])
      call(['git','pull'])
      return "OK"
    else: return "invalid credentials!"

if __name__ == "__main__": 
  web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
  app = web.application(urls, globals())
  app.run()        
