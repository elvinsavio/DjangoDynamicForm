#/usr/bin/python3

from django.shortcuts import render
import json
from django.http import HttpResponse

def load(name):
    try:
        f = open('./static/drug'+name+'.json','r')
        data = json.load(f)
        line = sorted(data['fields'], key=lambda k: k.get('order', 0)) #ordering json
        return line
    except:
        print(f'Error')

def index(request):
    return render(request, 'index.html')



def form(request, drug):
    return render(request, 'form.html', {"form":load(drug)})
