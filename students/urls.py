from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("welcome/", views.welcome),
    path("list/", views.list),
    path("currency/", views.currency),
    path("country/", views.country),
    path("countryinfo/", views.countryinfo),
    path("addcourse/", views.addcourse),
    path("addtopic/", views.addtopic),
    path("listcourses/", views.listcourses),
    re_path(r"topics/(\d+)", views.listtopics),
    path(r"ajax/", views.ajaxdemo),
    path(r"coursecount/", views.coursecount),
    path(r"searchcourses/", views.searchcourses),
    re_path(r"search/(\w+)", views.search),
]
