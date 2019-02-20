from flask import Flask
import platform
import datetime
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'user'
app.config['MYSQL_DATABASE_DB'] = 'pantest'
app.config['MYSQL_DATABASE_HOST'] = '172.20.0.5'

mysql.init_app(app)

@app.route("/")
def mypan():
  try:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM ptable")
    row = '<p> connect to db pantest: ' + ''.join(cursor.fetchone()) + '</p>'
#	date_time = '<p> ' + datetime.datetime.now() + '</p>'
    conn.commit()  
    conn.close()
  except Exception:
    row = '<p> Error connect to db pantest.</p>'
  return "<!DOCTYPE html><b>Nginx+Gunicorn+Flask on server: </b>" + platform.platform() + row 

if __name__ == "__main__":
  app.run()
