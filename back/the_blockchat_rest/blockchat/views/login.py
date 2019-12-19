from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden


def login(request):
    # return HttpResponse("")
    return HttpResponseForbidden()
