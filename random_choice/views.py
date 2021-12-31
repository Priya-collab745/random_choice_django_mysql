from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

#from . models import Question, Choice

# Get questions and display them
from django.shortcuts import render

def index(request):
  return render(request, 'index.html')