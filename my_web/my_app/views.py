from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Gwyneth C. Manuel BSIT-3")