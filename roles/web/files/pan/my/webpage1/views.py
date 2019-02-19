from django.shortcuts import render
import platform
import datetime
from django.db import connection
cursor = connection.cursor()


# Create your views here.

def webpage1(request):
    rows = 0
    srv_name = platform.platform()
    date_time = datetime.datetime.now()
    for row in cursor.execute("SELECT * FROM ptable"):
        rows=row
        
    if rows == 0:
        on_off = 'offline'
    else: on_off = 'online'
    
    return render(request, "./webpage1.html", locals())
