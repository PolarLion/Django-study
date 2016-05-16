# -*- coding: utf-8 -*- 
import logging

#logging.basicConfig(level=logging.INFO,format="%(asctime)s: %(name)s: %(levelname)s: %(message)s")
#logger = logging.getLogger(__name__)
#logfile = logging.FileHandler("/usr/share/Django-study/mysite/views.log")
#logfile.setFormatter(logging.Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s"))
#3logger.addHandler(logfile)

import sys
import socket


from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import time


def save_query(str_from, str_query, str_return, ttype, logfilename="query.log"):
  logfile = open(logfilename, 'a')
  logfile.write('\n')
  logfile.write(str(time.strftime('%Y-%m-%d %X',time.localtime(time.time()))).strip()+'\t')
  logfile.write("from: "+str_from+'\t')
  logfile.write('query: '+str_query.encode('utf-8','replace')+'\t'+ttype+'\t')
  logfile.write("return: "+str_return)
  logfile.close()

def index(request):
  return render_to_response('index.html', {'IMAGES_URL': '/static/images/', 'JS_URL':'/static/js/', 'CSS_URL':'/static/css/'})
  #return render_to_response('starter-template/index.html', {})

def contact_page(request):
  return render_to_response('contactpage.html', {'STATIC_URL': '/static/'})

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

def nmt(request, a):
  query = a.split('<sp>')[0]
  # print "!!!!!!", a
  ip = a.split('<sp>')[1]
  #return HttpResponse("ssss")
  host="127.0.0.1"
  port=8888
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.connect((host, port))


  if query == '':
    s.close()
    return HttpResponse("")
  source = query.encode('utf-8')
  s.sendall(source)
  data=s.recv(100000)
  target, align = eval(data)
  s.close()
  align.append(target)
  align.append(seg(source))
  print align
  # print "data", data
  re = repr(align).replace('\\x','%')
  save_query(str_from=ip, str_query=query, str_return=re, ttype="nmt")
  return HttpResponse(re)
  # return HttpResponse(repr(align))

def post(url, data):
  import urllib2
  req = urllib2.Request(url)  
  #enable cookie  
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
  response = opener.open(req, data)  
  return response.read() 

def smt(request, s):
  # print "request", request
  query = s.split('<sp>')[0]
  ip = s.split('<sp>')[1]
  import re
  import copy
  src = seg(query.encode('utf-8','replace'))
  new_line = ' '.join(src).strip()
  # print "!!!!!!!!!!!!!!!!!", a
  data = "<methodCall><methodName>translate</methodName><params><param><value><struct><member><name>text</name><value><string>"+new_line+"</string></value></member><member><name>align</name><value><string>1</string></value></member></struct></value></param></params></methodCall>"

  r = post("http://0.0.0.0:9999/RPC2", data)
  text=""
  print type(r), r
  # r = requests.post("http://0.0.0.0:9999/RPC2", data=data)
  p1 = re.compile(r'(?:(.|\n)*?)<string>(.*?)</string>(?:(.|\n)*)')
  p2 = re.compile(r'\s*\|\d+-\d+\|\s*')
  p3 = re.compile(r'\|(\d+)-(\d+)\|\s*')
  m1 = p1.findall(r)
  
  print r
  if len(m1)>0:
    text = m1[0][1]
    # print text
  m2 = p2.split(text)
  m2 = m2[:-1]
  m3 = p3.findall(text)
  print "m2", m2
  print "m3", m3
  align = []
  target = []
  temp = []
  for j in range(len(src)):
    temp.append(0.)
  for i in range(len(m2)):
    print m2[i].split(' ')
    ttarget = m2[i].split(' ')
    for ii in range(len(ttarget)):
      target.append(ttarget[ii])
      ttemp = copy.deepcopy(temp)
      for iii in range(int(m3[i][0]), int(m3[i][1])+1):
        ttemp[iii] = 0.85
      align.append(ttemp)

  align.append(target)
  align.append(src)
  print align
  re = repr(align).replace('\\x','%')
  save_query(str_from=ip, str_query=query, str_return=re, ttype="smt")
  return HttpResponse(re)



