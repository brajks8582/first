from django.shortcuts import render
from django.http import HttpResponse

def profile(request,username):
    return HttpResponse('<h1>this is the profile page,the user is  {}.</h1>'.format(username))


# Create your views here.
