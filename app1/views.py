from django.shortcuts import render
from django.http import HttpResponse

def say_salam(request):
    return HttpResponse("As salam u alaikum") 
