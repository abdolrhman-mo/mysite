from django.shortcuts import render
import datetime


def index(request):

    now = datetime.datetime.now().month == 1 and datetime.datetime.now().day == 1
    return render(
        request,
        'newyear/index.html',
        {
            'newyear': now
        }
    )
