# -*- coding: utf-8 -*- 

import time
import socket
import commands


SEPARATOR='<sp>'

def save_query(ttype, languages="error", str_from="error", str_query="error", str_return="error", logfilename="/home/xwshi/project/py/Django-study/mysite/query.log"):
  logfile = open(logfilename, 'a')
  logfile.write('\n')
  logfile.write(str(time.strftime('%Y-%m-%d %X',time.localtime(time.time()))).strip()+'\t')
  logfile.write("from: "+str_from+'\t')
  logfile.write('query: '+str_query+'\t'+languages+'\t'+ttype+'\t')
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


def nmt_caller(query, ip, languages):
  if query == '':
    save_query(ttype="nmt", str_from=ip, str_query=query)
    return ''

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("127.0.0.1", 8888))
  s.sendall(query+SEPARATOR+languages)
  data=s.recv(100000)
  s.close()

  source, target, align = eval(data)
  align.append(target)
  align.append(source.split(' '))
  # print "align", align
  # print "target", target
  res = repr(align).replace('\\x','%')
  save_query(str_from=ip, str_query=source, str_return=res, languages=languages, ttype="nmt")
  return res


def smt_caller(query, ip, languages):
  smt_server = {"zh-en":"http://0.0.0.0:9999/RPC2"}
  
  import re
  import copy
  
  src = ['']

  p1 = re.compile(r'(?:(.|\n)*?)<string>(.*?)</string>(?:(.|\n)*)')
  p2 = re.compile(r'\s*\|\d+-\d+\|\s*')
  p3 = re.compile(r'\|(\d+)-(\d+)\|\s*')
  if languages == "zh-en":
    src = seg(query)
    new_line = ' '.join(src).strip()
    data = "<methodCall><methodName>translate</methodName><params><param><value><struct><member><name>text</name><value><string>"+new_line+"</string></value></member><member><name>align</name><value><string>1</string></value></member></struct></value></param></params></methodCall>"

    r = post(smt_server[languages], data)
    text=""
    # print type(r), r
    
    m1 = p1.findall(r)
    if len(m1)>0:
      text = m1[0][1]
      # print "text", text
    # print text
  elif languages == "en-zh":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 8888))

    s.sendall(query+SEPARATOR+languages)
    data=s.recv(100000)
    s.close()

    source, _, _, = eval(data)
    src = source.split(' ')
    # print "untils.py en-zh src", src
    # print "en-zh"
    string = "echo \""+source+"\" | nc 127.0.0.1 3120"
    # print string
    (num, text) = commands.getstatusoutput(string)

    # print text

  m2 = p2.split(text)
  m2 = m2[:-1]
  m3 = p3.findall(text)
  # print "m2", m2
  # print "m3", m3
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
  # print align
  re = repr(align).replace('\\x','%')
  save_query(str_from=ip, str_query=query, languages=languages, str_return=re, ttype="smt")
  return re



