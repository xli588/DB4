from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    a = "Hello"
    b = " World"
    print("Inside hello function")
    return a + b
    
@app.route("/newpage")
def newPage():
    a = 1
    b = 2
    c = a + b
    return str(c)

@app.route("/mysql")    
def helloMySQL():
    cnx = mysql.connector.connect(user='root', database='6a')
    cursor = cnx.cursor()
    
    query = ("select * from AA")
    cursor.execute(query)
    
    returnString = []
    for i in cursor:
        print(i)
        returnString.append(i)
        
    cursor.close()
    cnx.close()
    return str(returnString)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)