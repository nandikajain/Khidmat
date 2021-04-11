import mysql.connector
from flask import Flask, render_template, redirect, url_for, request
app = Flask("__main__")


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="test",
  database="khidmatDB"
)

@app.route("/")
def custhome():
	mycursor = mydb.cursor()
	mycursor.execute("Select r.name, r.description, r.city, r.type, a.av from Restaurant r, (Select restaurantID, avg(ratings) as av from Rates group by restaurantID)a where a.restaurantID = r.restaurantID;")
	myresult = mycursor.fetchall()
	return render_template("index.html", x = myresult)

@app.route("/profile")
def custprof():
	user = '8799973366'
	mycursor = mydb.cursor()
	mycursor.execute(f"Select * from Customer where phone = '{user}'")
	myresult = mycursor.fetchall()
	return render_template("profile.html", x = myresult)


@app.route("/orders")
def pastorders():
	user = '8799973366'
	mycursor = mydb.cursor()
	mycursor.execute(f"Select o.orderID, o.customerID, o.restaurantID, o.billAmt, o.tip, o.status, o.dateTime, o.paymentMode, r.name from Orders o, Restaurant r where o.restaurantID = r.restaurantID and customerID = '{user}'")
	myresult = mycursor.fetchall()
	return render_template("orders.html", x = myresult)

if __name__ == "__main__":
	app.run()
	app.secret_key = "hello"
