#from django.shortcuts import render
#import platform
#import datetime
#import MySQLdb
#import mysql.connector as mariadb


#conn = MySQLdb.connect('172.20.0.5', 'user', 'user', 'pantest')
#cursor = conn.cursor()
#mariadb_connection = mariadb.connect(user='user', password='user', database='pantest')
#cursor = mariadb_connection.cursor()

#cursor.execute("SELECT * FROM ptable")
#rows = str(cursor.fetchone())
# Create your views here.


"""
def webpage1(request):
    conn = MySQLdb.connect('172.20.0.5', 'user', 'user', 'pantest')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ptable")
	rows = str(cursor.fetchone())
    srv_name = platform.platform()
    date_time = datetime.datetime.now()
 #   for row in cursor.execute("SELECT * FROM ptable"):
 #       rows=row
        
    if rows == 0:
        on_off = 'offline'
    else: on_off = 'online'
    
    return render(request, "./webpage1.html", locals())
"""
from my.webpage1.models import Person
from django.shortcuts import render_to_response, get_object_or_404
 
def index(request):
    person = Person()
    person.name = 'Alex'
    person.email = 'Alex@gmail.com'
    return render_to_response('person.html', {'p': person})
