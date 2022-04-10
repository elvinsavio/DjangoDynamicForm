#/usr/bin/python3

from django.shortcuts import render
import json
from django.http import HttpResponse

f1 = open('./static/drug1.json','r') #load local
f2 = open('./static/drug2.json','r') #load local


def index(request):
    return render(request, 'index.html')

def load(name):
    try:
        f = open('./static/drug'+name+'.json','r')
        data = json.load(f)
    except:
        print(f'Error')
    return data


def form(request, drug):
    return render(request, 'form.html', {"form":load(drug)})
