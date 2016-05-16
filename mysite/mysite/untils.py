# -*- coding: utf-8 -*- 

import time



def save_query(ttype, str_from="error", str_query="error", str_return="error", logfilename="query.log"):
  logfile = open(logfilename, 'a')
  logfile.write('\n')
  logfile.write(str(time.strftime('%Y-%m-%d %X',time.localtime(time.time()))).strip()+'\t')
  logfile.write("from: "+str_from+'\t')
  logfile.write('query: '+str_query.encode('utf-8','replace')+'\t'+ttype+'\t')
  logfile.write("return: "+str_return)
  logfile.close()

def seg(s):
  words = s.decode("utf-8", 'replace')
  new_line = []
  state=0
  for word in words:
    ch = word.encode('utf-8')
    # ch = word
    if (ch.isalnum() or ch == '.') and state == 0:
      new_line.append(ch) 
      state = 1
    elif state == 1 and (ch.isalnum() or ch == '.'):
      new_line.append(ch)
    elif ch.isspace():
      a = 0
    elif not ch.isalnum():
      state = 0
      new_line.append(ch)
  return new_line


def post(url, data):
  import urllib2
  req = urllib2.Request(url)  
  #enable cookie  
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
  response = opener.open(req, data)  
  return response.read() 