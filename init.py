from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

### main page ###
@app.route("/")
def Welcome():
    return render_template('Welcome.html')

@app.route("/Staff")
def Staff():
    return render_template('Staff.html')

@app.route("/Guest")
def Guest():
    return render_template('Guest.html')

### level 1 ###
@app.route("/Movie")
def Movie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Movie")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('Movie.html',users=users)


@app.route("/Genre")

def Genre():
    
   cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    
   cursor = cnx.cursor()
    
   query = ("SELECT * from Genre")
    
   cursor.execute(query)
    
   users=cursor.fetchall()
    
   cnx.close()
    
   return render_template('Genre.html',users=users)


@app.route("/Showing")

def Showing():
    
   cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    
   cursor = cnx.cursor()
    
   query = ("SELECT * from Showing")
    
   cursor.execute(query)
    
   users=cursor.fetchall()
    
   cnx.close()
    
   return render_template('Showing.html',users=users)


@app.route("/Customer")

def Customer():
    
   cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    
   cursor = cnx.cursor()
    
   query = ("SELECT * from Customer")
    
   cursor.execute(query)
    
   users=cursor.fetchall()
    
   cnx.close()
    
   return render_template('Customer.html',users=users)


@app.route("/Attend")

def Attend():
    
   cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    
   cursor = cnx.cursor()
    
   query = ("SELECT * from Attend")
    
   cursor.execute(query)
    
   users=cursor.fetchall()
    
   cnx.close()
    
   return render_template('Attend.html',users=users)

@app.route("/TheatreRoom")

def TheatreRoom():
    
   cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    
   cursor = cnx.cursor()
    
   query = ("SELECT * from TheatreRoom")
    
   cursor.execute(query)
    
   users=cursor.fetchall()
    
   cnx.close()
    
   return render_template('TheatreRoom.html',users=users)

### level 2 Movie ###

@app.route('/enterMoviename')
def MovieName(name=None):
    return render_template('formMovie.html', name=name)

@app.route('/Moviesubmit', methods=["POST"])
def Moviesubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Movie ( MovieName, MovieYear) "
        "VALUES (%s, %s)"
    )
    data = ( request.form['moviename'], request.form['movieyear'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('indexMovie.html', moviename=request.form['moviename'], movieyear=request.form['movieyear'])

@app.route('/Moviedelete/<data>')
def Moviedelete(data):
   moviename=data.split('_')[1]
   movieyear=data.split('_')[2]
   cnx=mysql.connector.connect(user='root', database='MovieTheatre')
   cursor=cnx.cursor()
   delete_stmt=("delete from Movie Where MovieName=\'"+moviename+"\' and MovieYear=\'"+movieyear+"\'")
   cursor.executr(delete_stmt,data)
   query=("select MovieName, MovieYear from Movie order by MovieName")
   returnList=[]
   try:
     cursor.execute(query)
   except:
     return render_template('Movie.html', results=returnList)
   for i in cursor:
     returnList.append([i[0],i[1],i[2], bytes.decode(i[3])])
   cnx.commit()
   cursor.close()
   cnx.close()
   return render_template('Movie.html', results=returnList)
    


@app.route('/Moviemodify', methods=["POST"])

def Moviemodify():
    
    id = request.args.get('id')
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()   
    modify_stmt = (
"UPDATE Movie SET MovieName = %s, MovieYear = %s WHERE idMovie = %s;"
)
   
    print(request.form.items)
    
    data = (request.form['moviename'], request.form['movieyear'], id)
 
    cursor.execute(modify_stmt, data)  
    cnx.commit()
    
    cnx.close()
   
    return render_template('modifyMovie.html', name=name)


@app.route('/sqlInjectionMovie')
def sqlInjectionMovie(name=None):
    return render_template('form2Movie.html')

@app.route('/submitSqlInjectionMovie', methods=["POST"])
def sqlInjectionResultMovie():
    cnx = mysql.connector.connect(user='root',database='MovieTheatre')
    cursor = cnx.cursor()
    moviename = request.form['moviename']
    query = ("SELECT * from Movie where moviename = '" + MovieName + "'")
    cursor.execute(query)
    print("Attempting: " + query)
    users=cursor.fetchall()

    cnx.commit()
    cnx.close()
    return str(users)


### level 2 Customer ###
@app.route('/enterCustomername')
def CustomerName(name=None):
    return render_template('formCustomer.html', name=name)

@app.route('/Customersubmit', methods=["POST"])
def Customersubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Customer (idCustomer, FirstName, LastName, EmailAddress, Sex) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    data = (request.form['customerid'],request.form['firstname'], request.form['lastname'], request.form['email'], request.form['sex'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('indexCustomer.html', customerid=request.form['customerid'], firstname=request.form['firstname'], lastname=request.form['lastname'], email=request.form['email'], sex=request.form['sex'])

@app.route("/Customerdelete/<data>")
def Customerdelete(data):
   idCustomer = request.args.get('Customerid')
   cnx=mysql.connector.connect(user='root', database='MovieTheatre')
   cursor=cnx.cursor()
   delete_stmt=("delete from Customer Where idCustomer='%s;'")
   data=(idCustomer,)
   cursor.executr(delete_stmt,data)
   query=("select FirstName, LastName, EmailAddress, Sex from Customer order by LastName")
   returnList=[]
   try:
     cursor.execute(query)
   except:
     return render_template('Customerdelete.html', results=returnList)
   for i in cursor:
     returnList.append([i[0],i[1],i[2], bytes.decode(i[3])])
   cnx.commit()
   cursor.close()
   cnx.close()
   return render_template('Customer.html', results=returnList)

@app.route('/Customermodify', methods=["POST"])

def Customermodify():
    
    customerid = request.args.get('customerid')
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()   
    modify_stmt = (
"UPDATE Customer SET LastName = %s, FirstName = %s, EmailAddress=%s, Sex=%s WHERE idCustomer = %s;"
)
   
    print(request.form.items)
    
    data = (request.form['firstname'], request.form['lastname'], request.form['email'], request.form['sex'])
 
    cursor.execute(modify_stmt, data)  
    cnx.commit()
    
    cnx.close()
   
    return render_template('modifyCustomer.html',request.form['firstname'], request.form['lastname'], request.form['email'], request.form['sex'] )

@app.route('/sqlInjectionCustomer')
def sqlInjectionCustomer(name=None):
    return render_template('form2Customer.html')

@app.route('/submitSqlInjectionCustomer', methods=["POST"])
def sqlInjectionResultCustomer():
    cnx = mysql.connector.connect(user='root',database='MovieTheatre')
    cursor = cnx.cursor()
    firstName = request.form['firstname']
    query = ("SELECT * from Customer where firstname = '" + firstName + "'")
    cursor.execute(query)
    print("Attempting: " + query)
    users=cursor.fetchall()

    cnx.commit()
    cnx.close()
    return str(users)


### level 2 Genre ###
@app.route('/enterGenrename')
def GenreName(name=None):
    return render_template('formGenre.html', name=name)

@app.route('/Genresubmit', methods=["POST"])
def Genresubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Genre (Genre,  Movie_idMovie) "
        "VALUES (%s, %s)"
    )
    data = ( request.form['genre'], request.form['movieid'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('indexGenre.html', genre=request.form['genre'], movieid=request.form['movieid'])

@app.route("/Genredelete/<data>")
def Genredelete(data):
   movieid = request.args.get('movieid')
   cnx=mysql.connector.connect(user='root', database='MovieTheatre')
   cursor=cnx.cursor()
   delete_stmt=("delete from Genre Where Movie_idMovie='%s;'")
   data=(movieid,)
   cursor.executr(delete_stmt,data)
   query=("select Genre, Movie_idMovie from Genre")
   returnList=[]
   try:
     cursor.execute(query)
   except:
     return render_template('Genredelete.html', results=returnList)
   for i in cursor:
     returnList.append([i[0],i[1],i[2], bytes.decode(i[3])])
   cnx.commit()
   cursor.close()
   cnx.close()
   return render_template('Genre.html', results=returnList)

@app.route('/Genremodify', methods=["POST"])

def Genremodify():
    
    movieid = request.args.get('movieid')
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()   
    modify_stmt = (
"UPDATE Genre SET Genre = %s, Movie_idMovie = %s;"
)
   
    print(request.form.items)
    
    data = (request.form['genre'], request.form['movieid'])
 
    cursor.execute(modify_stmt, data)  
    cnx.commit()
    
    cnx.close()
   
    return render_template('modifyGenre.html',request.form['genre'], request.form['movieid'] )

@app.route('/sqlInjectionGenre')
def sqlInjection(name=None):
    return render_template('form2Genre.html')

@app.route('/submitSqlInjectionGenre', methods=["POST"])
def sqlInjectionResultGenre():
    cnx = mysql.connector.connect(user='root',database='MovieTheatre')
    cursor = cnx.cursor()
    genre = request.form['genre']
    query = ("SELECT * from Genre where genre = '" + genre + "'")
    cursor.execute(query)
    print("Attempting: " + query)
    users=cursor.fetchall()

    cnx.commit()
    cnx.close()
    return str(users)

### level 2 Attend ###
@app.route('/enterAttendname')
def AttendName(name=None):
    return render_template('formAttend.html', name=name)

@app.route('/Attendsubmit', methods=["POST"])
def Attendsubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Attend (Customer_idCustomer,Showing_idShowing , Rating) "
        "VALUES (%s, %s, %s)"
    )
    data = ( request.form['customerid'], request.form['showingid'], request.form['rating'] )
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('indexAttend.html', customerid=request.form['moviename'])

@app.route("/Attenddelete/<data>")
def Attenddelete(data):
   customerid = request.args.get('customerid')
   cnx=mysql.connector.connect(user='root', database='MovieTheatre')
   cursor=cnx.cursor()
   delete_stmt=("delete from Attend Where Customer_CustomerId='%s'")
   cursor.executr(delete_stmt,data)
   query=("select Attend, Movie_idMovie from Attend")
   returnList=[]
   try:
     cursor.execute(query)
   except:
     return render_template('Attenddelete.html', results=returnList)
   for i in cursor:
     returnList.append([i[0],i[1],i[2], bytes.decode(i[3])])
   cnx.commit()
   cursor.close()
   cnx.close()
   return render_template('Attend.html', results=returnList)

@app.route('/Attendmodify', methods=["POST"])

def Attendmodify():
    
    movieid = request.args.get('movieid')
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()   
    modify_stmt = (
"UPDATE Attend SET Genre = %s, Movie_idMovie = %s;"
)
   
    print(request.form.items)
    
    data = (request.form['customerid'], request.form['showingid'], request.form['rating'])
 
    cursor.execute(modify_stmt, data)  
    cnx.commit()
    
    cnx.close()
   
    return render_template('modifyAttend.html',request.form['customerid'], request.form['showingid'], request.form['rating'])

@app.route('/sqlInjectionAttend')
def sqlInjectionAttend(name=None):
    return render_template('form2Attend.html')

@app.route('/submitSqlInjectionAttend', methods=["POST"])
def sqlInjectionResultAttend():
    cnx = mysql.connector.connect(user='root',database='MovieTheatre')
    cursor = cnx.cursor()
    customerid = request.form['customerid']
    query = ("SELECT * from Attend where customerid = '" + customerid + "'")
    cursor.execute(query)
    print("Attempting: " + query)
    users=cursor.fetchall()

    cnx.commit()
    cnx.close()
    return str(users)

### level 2 Showing ###
@app.route('/enterShowingname')
def ShowingName(name=None):
    return render_template('formShowing.html', name=name)

@app.route('/Showingsubmit', methods=["POST"])
def Showingsubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Showing ( idShowing, ShowingDateTime, Movie_idMovie,  TheatreRoom_RoomNumber , TicketPrice) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    data = ( request.form['showingid'], request.form['showingdatetime'], request.form['movieid'], request.form['roomnumber'],request.form['ticketprice'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('indexShowing.html', showingid=request.form['showingid'], showingdatetime=request.form['showingdatetime'], movieid=request.form['movieid'],roomnumber= request.form['roomnumber'],ticketprice=request.form['ticketprice'])

@app.route("/Showingdelete/<data>")
def Showingdelete(data):
   showingid = request.args.get('showingid')
   cnx=mysql.connector.connect(user='root', database='MovieTheatre')
   cursor=cnx.cursor()
   delete_stmt=("delete from Showing Where ShowingID='%s'")
   cursor.executr(delete_stmt,data)
   query=("select ShowingID, ShowingDateTime, MovieID, RoomNumber, TicketPrice from Showing")
   returnList=[]
   try:
     cursor.execute(query)
   except:
     return render_template('Showingdelete.html', results=returnList)
   for i in cursor:
     returnList.append([i[0],i[1],i[2], bytes.decode(i[3])])
   cnx.commit()
   cursor.close()
   cnx.close()
   return render_template('Showing.html', results=returnList)

@app.route('/Showingmodify', methods=["POST"])

def Showingmodify():
    
    showingid = request.args.get('showingid')
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()   
    modify_stmt = (
"UPDATE Showing SET Showingid = %s, Movie_idMovie = %s;"
)
   
    print(request.form.items)
    
    data = (request.form['showingid'], request.form['showingdatetime'], request.form['movieid'], request.form['roomnumber'], request.form['ticketprice'])
 
    cursor.execute(modify_stmt, data)  
    cnx.commit()
    
    cnx.close()
   
    return render_template('modifyShowing.html',request.form['showingid'], request.form['showingdatetime'], request.form['movieid'], request.form['roomnumber'], request.form['ticketprice'])

@app.route('/sqlInjectionShowing')
def sqlInjectionShowing(name=None):
    return render_template('form2Showing.html')

@app.route('/submitSqlInjectionShowing', methods=["POST"])
def sqlInjectionResultShowing():
    cnx = mysql.connector.connect(user='root',database='MovieTheatre')
    cursor = cnx.cursor()
    showingid = request.form['showingid']
    query = ("SELECT * from Showing where showingid = '" + showingid + "'")
    cursor.execute(query)
    print("Attempting: " + query)
    users=cursor.fetchall()

    cnx.commit()
    cnx.close()
    return str(users)

### level 2 TheatreRoom ###
@app.route('/enterTheatreRoomname')
def TheatreRoomName(name=None):
    return render_template('formTheatreRoom.html', name=name)

@app.route('/TheatreRoomsubmit', methods=["POST"])
def TheatreRoomsubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO TheatreRoom (RoomNumber, Capacity) "
        "VALUES (%s, %s)"
    )
    data = ( request.form['roomnumber'], request.form['capacity'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('indexTheatreRoom.html', roomnumber=request.form['roomnumber'], capacity= request.form['capacity'])

@app.route("/Theatredelete/<data>")
def Theatredelete(data):
   roomnumber = request.args.get('roomnumber')
   cnx=mysql.connector.connect(user='root', database='MovieTheatre')
   cursor=cnx.cursor()
   delete_stmt=("delete from Showing Where RoomNumber='%s'")
   cursor.executr(delete_stmt,data)
   query=("select RoomNumber, Capacity from Showing")
   returnList=[]
   try:
     cursor.execute(query)
   except:
     return render_template('TheatreRoomdelete.html', results=returnList)
   for i in cursor:
     returnList.append([i[0],i[1],i[2], bytes.decode(i[3])])
   cnx.commit()
   cursor.close()
   cnx.close()
   return render_template('TheatreRoom.html', results=returnList)

@app.route('/TheatreRoommodify', methods=["POST"])

def TheatreRoommodify():
    
    roomnumber = request.args.get('roomnumber')
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()   
    modify_stmt = (
"UPDATE TheatreRoom SET RoomNumber = %s, Capacity = %s;"
)
   
    print(request.form.items)
    
    data = (request.form['roomnumber'], request.form['capacity'])
 
    cursor.execute(modify_stmt, data)  
    cnx.commit()
    
    cnx.close()
   
    return render_template('modifyTheatreRoom.html',request.form['roomnumber'], request.form['capacity'])
 

@app.route('/sqlInjectionTheatreRoom')
def sqlInjectionTheatreRoom(name=None):
    return render_template('form2TheatreRoom.html')

@app.route('/submitSqlInjectionTheatreRoom', methods=["POST"])
def sqlInjectionResultTheatreRoom():
    cnx = mysql.connector.connect(user='root',database='MovieTheatre')
    cursor = cnx.cursor()
    RoomNumber = request.form['roomnumber']
    query = ("SELECT * from TheatreRoom where roomnumber= '" + roomnumber + "'")
    cursor.execute(query)
    print("Attempting: " + query)
    users=cursor.fetchall()

    cnx.commit()
    cnx.close()
    return str(users)

###Guest###
@app.route("/GuestSearch")
def Search():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT distinct Genre from Genre")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('GuestSearch.html',users=users)

@app.route("/GuestSearchDate")
def SearchDate():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select distinct date(ShowingDateTime) from Showing")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('GuestSearchDate.html',users=users)

@app.route("/GuestSearchEndDate")
def SearchEndDate():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select distinct date(ShowingDateTime) from Showing")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('GuestSearchEndDate.html',users=users)

@app.route("/GuestSearchSeat")
def SearchSeat():
    return render_template('GuestSearchSeat.html')

@app.route("/GuestSearchTitle")
def SearchTitle():
    return render_template('GuestSearchTitle.html')

@app.route("/GuestAttend")
def GuestAttend():    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT FirstName,LastName from Customer")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('GuestAttend.html',users=users)

@app.route("/GuestAttendShowing")
def GuestAttendShowing():    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select * from Showing")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('GuestAttendShowing.html',users=users)

@app.route("/GuestRate")
def GuestRate():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT FirstName,LastName from Customer")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('GuestRate.html',users=users)


@app.route("/GuestRateShowing")
def GuestRateShowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT Showing_idShowing from Attend")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('GuestRateShowing.html',users=users)


@app.route("/GuestRating")
def GuestRating():
    return render_template('GuestRating.html')

@app.route("/GuestViews")
def GuestViews():    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT FirstName,LastName from Customer")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('GuestViews.html',users=users)

@app.route("/GuestViewsSelect")
def GuestViewsSelect():    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT Showing_idShowing,Rating from Attend")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('GuestViewsSelect.html',users=users)

@app.route("/GuestProfile")
def GuestProfile():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT FirstName,LastName from Customer")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('GuestProfile.html',users=users)

@app.route("/GuestProfileShow")
def GuestProfileShow():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Customer")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('GuestProfileShow.html',users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
