from django.http import HTTPResopnse
from django.shortcuts import redirect

def index(request):
    return HTTPResponse('index')

def login(request):
    return redirect('/index')

