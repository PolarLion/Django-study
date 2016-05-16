# -*- coding: utf-8 -*- 


import sys

from django.http import HttpResponse
from django.shortcuts import render_to_response
from untils import *




def index(request):
  return render_to_response('index.html', {'IMAGES_URL': '/static/images/', 'JS_URL':'/static/js/', 'CSS_URL':'/static/css/'})
  #return render_to_response('starter-template/index.html', {})

def contactpage(request):
  return render_to_response('contactpage.html', {'IMAGES_URL': '/static/images/', 'JS_URL':'/static/js/', 'CSS_URL':'/static/css/'})

def nmt(request, a):
  struct = a.split('<sp>')
  print struct
  if len(struct) < 3:
    save_query(ttype="nmt")
    return HttpResponse("")

  query = struct[0]
  ip = struct[1]
  languages = struct[2]

  return HttpResponse(nmt_caller(query, ip, languages.encode('ascii', 'replace')))
  

def smt(request, a):
  struct = a.split('<sp>')
  print struct
  if len(struct) < 3:
    save_query(ttype="smt")
    return HttpResponse("")

  query = struct[0]
  ip = struct[1]
  languages = struct[2]

  return HttpResponse(smt_caller(query, ip, languages.encode('ascii', 'replace')))

