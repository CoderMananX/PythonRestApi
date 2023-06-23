from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# Create your views here.

def home_page(request):
    print("home page requested")
    friends = [
        'manan',
        'parth',
        'sahil',
    ]
    return JsonResponse(friends,safe=False)