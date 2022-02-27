from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Homepage(request):
    return render(request, 'index.html')
def Results(request):
    return render(request, 'results.html')
