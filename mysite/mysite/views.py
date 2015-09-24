from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import sys
# sys.path.remove("/home/xwshi/anaconda/pkgs/")
if not "/home/xwshi/project/py/GroundHog/experiments/nmt/" in sys.path:
  sys.path.append("/home/xwshi/project/py/GroundHog/experiments/nmt/")
if not "/home/xwshi/project/py/GroundHog/" in sys.path:
  sys.path.append("/home/xwshi/project/py/GroundHog/")
if not "/home/xwshi/anaconda/lib/python2.7/site-packages/" in sys.path:
  sys.path.append("/home/xwshi/anaconda/lib/python2.7/site-packages/")
# import translateserver

def current_datetime(request):
  now = datetime.datetime.now()
  #html = "<html><body>It is now %s.</body></html>" % now
  #return HttpResponse(html)
  return render_to_response('current_datetime.html', {'current_date': now})

def test_bootstrap(request):
  #html = open('starter-template/index.html')d
  #return HttpResponse('starter-template/index.html')
  return render_to_response('starter-template/index.html', {})

def nmt(request, a):
	words = a.encode('utf-8').decode("utf-8")
	state = 0
	new_line = ""
	for word in words:
		ch = word.encode('utf-8')
		if (ch.isalnum() or ch == '.') and state == 0:
			new_line += " " + ch
			state = 1
		elif state == 1 and (ch.isalnum() or ch == '.'):
			new_line += ch
		elif ch.isspace():
			a = 0
		elif not ch.isalnum():
			state = 0
			new_line += " " + ch
	new_line = new_line.strip()
	# return  HttpResponse(s)
	# return  HttpResponse(translateserver.translate(s))
  	# re =  translateserver.translate(ss)
  	# return  HttpResponse(new_line)
  	return  HttpResponse(translateserver.translate(new_line))


def bootstrap0(request):
  return render_to_response('index.html', {'STATIC_URL': '/static/'})
  #return render_to_response('starter-template/index.html', {})
