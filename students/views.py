from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Course
from .forms import AddCourseForm, AddTopicForm
import requests
from . import database

def ajaxdemo(request):
    return render(request, "ajax_demo.html")

def coursecount(request):
    count = database.get_course_count()
    return HttpResponse(count)


def searchcourses(request):
    return render(request, 'searchcourses.html')

def search(request,title):
    courses = database.get_courses_by_title(title)
    # print(courses)
    result = []
    for c in courses:
        result.append( {"title" : c[1], "fee" : c[3]})

    return JsonResponse(result, safe = False)


def listcourses(request):
    """
    Retrives all courses from Courses table
    """
    return render(request, 'listcourses.html', {"courses": database.get_courses()})

def listtopics(request,id):
    """
    id  is course id passed in url
    retrieves all topics for the given course id and make it available to template
    """
    topics = database.get_topics(id)
    print(len(topics))
    return render(request, 'listtopics.html', { 'topics' : topics})


def addcourse(request):
    # Get request, first present
    if request.method == "GET":
        f = AddCourseForm()  # unbound form
        return render(request, 'addcourse.html', {'form': f})
    else:
        # post request so process data
        f = AddCourseForm(request.POST)  # bound form
        if f.is_valid():
            title = f.cleaned_data["title"]
            duration = f.cleaned_data["duration"]
            fee = f.cleaned_data["fee"]
            print(title, duration, fee)
            # add course to COURSES table
            done = database.add_course(title, duration, fee)
            if done:
                message = "Added Course Successfully!"
            else:
                message = "Sorry! Could not add course!"
        else:
            message = "Sorry! Invalid Data!"

        return render(request, 'addcourse.html', {'form': f, "message": message})


def welcome(request):
    return render(request, 'welcome.html')


def country(request):
    return render(request, 'country.html')


def countryinfo(request):
    # get information about country
    code = request.GET["code"]
    resp = requests.get("https://restcountries.eu/rest/v2/alpha/" + code)
    if resp.status_code == 200:
        country = resp.json()
        return render(request, 'countryinfo.html', {"country": country})
    else:
        return render(request, 'countryinfo.html')


def list(request):
    courses = [Course("Angular", 15, 2000), Course("Java EE", 40, 5000)]
    return render(request, 'list.html', {"courses": courses})


def currency(request):
    if 'amount' in request.GET:
        amount = int(request.GET["amount"])
        usd = amount / 68
        return render(request, 'currency.html', {"amount": amount, "usd": usd})
    else:
        return render(request, 'currency.html')


def addtopic(request):
    f = AddTopicForm()
    return render(request, 'addtopic.html', { 'form' : f})
