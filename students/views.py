from django.shortcuts import render
from .models import Course
import requests

def welcome(request):
    return render(request, 'welcome.html')

def country(request):
    return render(request,'country.html')

def countryinfo(request):
    # get information about country
    code = request.GET["code"]
    resp = requests.get("https://restcountries.eu/rest/v2/alpha/" + code)
    if resp.status_code == 200:
        country = resp.json()
        return render(request,'countryinfo.html', { "country" : country })
    else:
        return render(request, 'countryinfo.html')

def list(request):
    courses = [Course("Angular", 15, 2000), Course("Java EE", 40, 5000)]
    return render(request, 'list.html' , { "courses" : courses})

def currency(request):
    if 'amount' in request.GET:
        amount = int(request.GET["amount"])
        usd = amount / 68
        return render(request, 'currency.html', {"amount" : amount, "usd" : usd})
    else:
        return render(request, 'currency.html')