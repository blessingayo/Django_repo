"""firstdjangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


# def print_hello_world(self):
#     print("Hello World")
#     return HttpResponse("Hello world")

def register(self):
    return HttpResponse("This is a registration page")


def login(self):
    return HttpResponse("This is a login page")


def update_a_native(self):
    return HttpResponse("Update a native page")


def list_natives(self):
    return HttpResponse("list native page")


def delete_a_native(self):
    return HttpResponse("delete a native")


def list_of_cohorts(self):
    return HttpResponse("A list of cohorts")


def create_a_cohorts(self):
    return HttpResponse("create a cohorts")


def update_a_cohorts(self):
    return HttpResponse("update cohorts")


def delete_a_cohorts(self):
    return HttpResponse("delete cohorts")


def home(self):
    return HttpResponse("Welcome home")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("natives/register", register),
    path("natives/login", register),
    path("natives/update", update_a_native),
    path("natives/", list_natives),
    path("natives/delete", delete_a_native),
    path("cohorts/", list_of_cohorts),
    path("cohorts/create", create_a_cohorts),
    path("cohorts/update", update_a_native),
    path("cohorts/delete", delete_a_cohorts),
    path('', home),
]


def hello_world(self):
    print("Hello World!")
