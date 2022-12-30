from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def newlife(request):
    return HttpResponse('Iam starting new life today')




def newyear(request):
    return HttpResponse('because the new year coming')
