from django.shortcuts import render
from django.http import HttpResponse

def test_function(request):
    return HttpResponse("Test function is working")