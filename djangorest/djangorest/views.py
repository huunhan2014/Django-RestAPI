from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("Wellcome to my Project")