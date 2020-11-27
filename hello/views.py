from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'hello/index.html')


def Abdo(request):
    return HttpResponse('Hello, Abdo!')


def greet(request, name):
    # return HttpResponse(f'Hello, {name.capitalize()}')
    return render(
        request,
        'hello/name.html',
        {
            'name': name.capitalize()
        }
    )
