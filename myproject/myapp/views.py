from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    path = request.path
    return HttpResponse(path , content_type='text/html' , charset='utf-8')