from django.http import HTTPResopnse

def index(request):
    return HTTPResponse('index')
