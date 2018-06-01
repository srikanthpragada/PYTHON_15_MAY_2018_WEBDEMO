from django.shortcuts import render
from .models import Course


def welcome(request):
    return render(request, 'welcome.html')


def list(request):
    courses = [Course("Angular", 15, 2000), Course("Java EE", 40, 5000)]
    return render(request, 'list.html' , { "courses" : courses})
