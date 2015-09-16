from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
  now = datetime.datetime.now()
  #html = "<html><body>It is now %s.</body></html>" % now
  #return HttpResponse(html)
  return render_to_response('current_datetime.html', {'current_date': now})

def test_bootstrap(request):
  #html = open('starter-template/index.html')d
  #return HttpResponse('starter-template/index.html')
  return render_to_response('starter-template/index.html', {})
