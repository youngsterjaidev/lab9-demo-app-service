from flask import Flask
import mysql.connector
from dotenv import dotenv_values, load_dotenv

load_dotenv() 

config = dotenv_values(".env")

print(config)

mydb = mysql.connector.connect(
  host= config["DB_HOSTNAME"],
  user=config["DB_USERNAME"],
  password=config["DB_PASSWORD"]
)

print(mydb)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Lab9 :)</p>"

# send database names to user as a response
@app.route("/databases")
def fetch_databases():
    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES;")

    myresult = mycursor.fetchall()

    return myresult

if __name__ == "__main__":
    app.run(host="0.0.0.0")