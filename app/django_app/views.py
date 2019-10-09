from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request, id, name):
    result = 'あなたのidは' + str(id) + 'あなたの名前は' + name + "です。"

    return HttpResponse(result)