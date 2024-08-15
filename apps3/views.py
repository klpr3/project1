from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cinema(request):
    return HttpResponse('new movie release' )
    