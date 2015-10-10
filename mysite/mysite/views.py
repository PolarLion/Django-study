# -*- coding: utf-8 -*- 
import logging

#logging.basicConfig(level=logging.INFO,format="%(asctime)s: %(name)s: %(levelname)s: %(message)s")
#logger = logging.getLogger(__name__)
#logfile = logging.FileHandler("/usr/share/Django-study/mysite/views.log")
#logfile.setFormatter(logging.Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s"))
#3logger.addHandler(logfile)

import sys
import socket
#if not "/home/polarlion/GroundHog/experiments/nmt/" in sys.path:
  #sys.path.append("/home/polarlion/GroundHog/experiments/nmt/")
#if not "/home/polarlion/GroundHog/" in sys.path:
  #sys.path.append("/home/polarlion/GroundHog/")
#if not "/home/polarlion/GroundHog/experiments/" in sys.path:
  #sys.path.append("/home/polarlion/GroundHog/experiments/")
#if not "/home/xwshi/anaconda/lib/python2.7/site-packages/" in sys.path:
  #sys.path.append("/home/xwshi/anaconda/lib/python2.7/site-packages/")

#for path in sys.path:
  #logger.info(path)

#import translateserver


from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

class StreamToLogger(object):
  def __init__(self, logger, log_level=logging.INFO):
    self.logger = logger
    self.log_level = log_level
    self.linebuf = ''
  def write(self, buf):
    for line in buf.rstrip().splitlines():
      self.logger.log(self.log_level, line.rstrip())

#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',filename="/usr/share/Django-study/mysite/out.log",filemode='a')
#stdout_logger = logging.getLogger('STDOUT')
#sl = StreamToLogger(stdout_logger, logging.INFO)
#sys.stdout = sl
#stderr_logger = logging.getLogger('STDERR')
#sl = StreamToLogger(stderr_logger, logging.ERROR)
#sys.stderr = sl
#print "Test to standard out"
#raise Exception('Test to standard error')

#logstream = logging.StreamHandler(sys.stderr)
#logstream.setFormatter(formatter)
#logger.addHandler(logstream)

# sys.path.remove("/home/xwshi/anaconda/pkgs/")
#import hehe

def current_datetime(request):
  now = datetime.datetime.now()
  #html = "<html><body>It is now %s.</body></html>" % now
  #return HttpResponse(html)
  return render_to_response('current_datetime.html', {'current_date': now})

def test_bootstrap(request):
  #html = open('starter-template/index.html')d
  #return HttpResponse('starter-template/index.html')
  return render_to_response('starter-template/index.html', {})

#import module_nmt

def bootstrap0(request):
  return render_to_response('index.html', {'STATIC_URL': '/static/'})
  #return render_to_response('starter-template/index.html', {})

def nmt(request, a):
  host="127.0.0.1"
  port=8888
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.connect((host, port))
  ssss = "你好"
  #s.sendall(ssss)
  s.sendall(a.encode('utf-8'))
  data=s.recv(1024)                                                                                                                                                              
  s.close()
  return HttpResponse(str(data))

#print translateserver.translate("输 出")
