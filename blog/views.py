from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_list():
    return HttpResponse("Hello world")
