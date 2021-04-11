import mysql.connector
from flask import Flask, render_template, redirect, url_for, request
app = Flask("__main__")


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="test",
  database="khidmatDB"
)

@app.route("/customer/browse")
def custhome():
	mycursor = mydb.cursor()
	mycursor.execute("Select r.name, r.description, r.city, r.type, a.av from Restaurant r, (Select restaurantID, avg(ratings) as av from Rates group by restaurantID)a where a.restaurantID = r.restaurantID;")
	myresult = mycursor.fetchall()
	return render_template("index.html", x = myresult)

@app.route("/customer/profile")
def custprof():
	user = '8799973366'
	mycursor = mydb.cursor()
	mycursor.execute(f"Select * from Customer where phone = '{user}'")
	myresult = mycursor.fetchall()
	return render_template("profile.html", x = myresult)


@app.route("/customer/orders")
def pastorders():
	user = '8799973366'
	mycursor = mydb.cursor()
	mycursor.execute(f"Select o.orderID, o.customerID, o.restaurantID, o.billAmt, o.tip, o.status, o.dateTime, o.paymentMode, r.name from Orders o, Restaurant r where o.restaurantID = r.restaurantID and customerID = '{user}'")
	myresult = mycursor.fetchall()
	return render_template("orders.html", x = myresult)


@app.route("/donor/browse")
def donor_view():
	mycursor = mydb.cursor()
	mycursor.execute("Select * from Receiver;")
	myresult = mycursor.fetchall()
	return render_template("view_rec.html", x = myresult)

@app.route("/donor/profile")
def donor_prof():
	user = 'D1087302'
	mycursor = mydb.cursor()
	mycursor.execute(f"Select * from Donor where donorID = '{user}'")
	myresult = mycursor.fetchall()
	return render_template("donor_prof.html", x = myresult)


@app.route("/donor/donations")
def donor_donations():
	user = 'D1087302'
	mycursor = mydb.cursor()
	mycursor.execute(f"Select d.donationID, d.deliveryWorkerID, d.dateTime, d.category, d.status, d.quantity, r.name from Receiver r, Donation d where d.receiverID = r.receiverID and donorID = '{user}'")
	myresult = mycursor.fetchall()
	return render_template("past_donations.html", x = myresult)


@app.route("/delivery/profile")
def delivery_profile():
	user = 'E250818'
	mycursor = mydb.cursor()
	mycursor.execute(f"Select * from DeliveryWorker where employeeID = '{user}'")
	myresult = mycursor.fetchall()
	return render_template("delivery_profile.html", x = myresult)

@app.route("/delivery/")
def deliveries():
	user = 'E250898'
	mycursor = mydb.cursor()
	mycursor.execute(f"Select o.OrderID, r.name, r.street, r.city, r.state, r.pin, c.phone, c.hNo, c.street, c.area, c.city, c.pin, o.paymentMode, o.billAmt from Orders o, Restaurant r, Customer c where c.phone = o.customerID and r.restaurantID = o.restaurantID and o.deliveryWorkerID = '{user}'")
	myresult = mycursor.fetchall()
	mycursor.execute(f"Select d.donationID, do.phone, do.hNo, do.area, do.city, do.state, do.pin, r.name, r.street, r.area, r.city, r.state, r.pin from Donation d, Donor do, Receiver r where r.receiverID = d.receiverID and d.donorID = do.donorID and d.deliveryWorkerID = '{user}'")
	myresult2 = mycursor.fetchall()
	return render_template("deliveries.html", x = myresult, y = myresult2)


@app.route("/receiver/profile")
def receiver_prof():
	user = 'R320109'
	mycursor = mydb.cursor()
	mycursor.execute(f"Select * from Receiver where receiverID = '{user}'")
	myresult = mycursor.fetchall()
	return render_template("donor_prof.html", x = myresult)


@app.route("/receiver/donations")
def receiver_donations():
	user = 'R320109'
	mycursor = mydb.cursor()
	mycursor.execute(f"Select d.donationID, d.deliveryWorkerID, d.dateTime, d.category, d.status, d.quantity, r.name from Donor r, Donation d where d.donorID = r.donorID and receiverID = '{user}'")
	myresult = mycursor.fetchall()
	return render_template("past_donations.html", x = myresult)

@app.route("/management/profile")
def management_prof():
	user = 'S540992'
	mycursor = mydb.cursor()
	mycursor.execute(f"Select * from Management where employeeID = '{user}'")
	myresult = mycursor.fetchall()
	return render_template("management_prof.html", x = myresult)


if __name__ == "__main__":
	app.run()
	app.secret_key = "hello"
