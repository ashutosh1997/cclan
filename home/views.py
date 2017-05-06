from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext


def home(request):
    return render(request, "landing.html")


def about_us(request):
    return render(request, "about_us.html")
