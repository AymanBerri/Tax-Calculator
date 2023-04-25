from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

# Create your views here.

rate = 15

def index(request):
    return HttpResponse("<h1>This is a site to calculate tax</h1>")

def calc_tax(request, num):

    print(num)
    try:
        return HttpResponse(f"<h1>Your tax is ${float(num) + (float(num)*(rate/100)):,.4f}</h1>")
    except:
        return HttpResponse(f"<h1><span style='color:red;'>'{num}' is invalid.</span><br>Please input a number.</h1>")

def tax_rate(request):
    return HttpResponse(f"<h1>The current tax rate is {rate}%</h1>")