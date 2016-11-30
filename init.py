from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def Welcome():
    return render_template('Welcome.html')

@app.route("/Staff")
def Staff():
    return render_template('Staff.html')

@app.route("/guest")
def guest():
    return render_template('guest.html')

@app.route("/users")
def users():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Movie")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('users.html',users=users)

@app.route('/entername')
def helloName(name=None):
    return render_template('form.html', name=name)

@app.route('/submit', methods=["POST"])
def submit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Movies (MovieID, MovieName, MovieYear) "
        "VALUES (%s, %s, %s)"
    )
    data = (request.form['Movie ID'], request.form['Movie Name'], request.form['Movie Year'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('index.html', MovieName=request.form['Movie Name'])

@app.route('/sqlInjection')
def sqlInjection(name=None):
    return render_template('form2.html')

@app.route('/submitSqlInjection', methods=["POST"])
def sqlInjectionResult():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    firstName = request.form['firstname']
    query = ("SELECT * from Customer where firstname = '" + firstName + "'")
    cursor.execute(query)
    print("Attempting: " + query)
    users=cursor.fetchall()

    cnx.commit()
    cnx.close()
    return str(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)