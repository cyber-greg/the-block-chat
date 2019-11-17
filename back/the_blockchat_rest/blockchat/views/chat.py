from django.shortcuts import render
from django.http import HttpResponse


def chat(request):
    response = [
        {'id':'1','message':'hello API'},
        {'id':'2','message':'hello API 2'},
        {'id':'3','message':'hello API 3'},
        ]
    return HttpResponse(response)