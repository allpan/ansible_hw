from django.shortcuts import render
import platform
import datetime


# Create your views here.

def webpage1(request):
    date = "123"
    srv_name = platform.platform()
    on_off = 'offline'
    date_time = datetime.datetime.now()

    return render(request, "./webpage1.html", locals())
