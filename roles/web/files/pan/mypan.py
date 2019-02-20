from flask import Flask
import platform
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
    row = ' <p style="color:forestgreen;">' + ''.join(cursor.fetchone()) + "</p>"
	
    conn.commit()  
    conn.close()
  except Exception:
    row = '<p style="color:red;"> Error connect to db.</p>'
  return "<!DOCTYPE html><b>Hello World</b> from " + platform.platform() + row

if __name__ == "__main__":
  app.run()
