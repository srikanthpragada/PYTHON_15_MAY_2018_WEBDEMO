from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.welcome),
    path("list/", views.list),
    path("currency/", views.currency),
    path("country/", views.country),
    path("countryinfo/", views.countryinfo),
    path("addcourse/", views.addcourse),
    path("listcourses/", views.listcourses),
]
