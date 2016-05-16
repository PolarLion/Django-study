# -*- coding: utf-8 -*- 


import sys
import socket

from django.http import HttpResponse
from django.shortcuts import render_to_response
from untils import *




def index(request):
  return render_to_response('index.html', {'IMAGES_URL': '/static/images/', 'JS_URL':'/static/js/', 'CSS_URL':'/static/css/'})
  #return render_to_response('starter-template/index.html', {})

def contactpage(request):
  return render_to_response('contactpage.html', {'IMAGES_URL': '/static/images/', 'JS_URL':'/static/js/', 'CSS_URL':'/static/css/'})

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



