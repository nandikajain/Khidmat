from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta, datetime
from random import randint

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="nandikajain",passwd="3827", database="khidmatDB" )
app = Flask (__name__)
app.permanent_session_lifetime = timedelta(days = 1)
app.secret_key = "khidmatDB"
mycursor = mydb.cursor()



@app.route("/", methods= ["POST", "GET"])
def login():
    if(request.method == "GET"):
        return render_template("login.html")
    else:
        print(request.form)
        username = request.form["username"]
        password = request.form["password"]
        typeOf = request.form["typeOf"] 
        q=""
        if(typeOf == "Customer"):
            q=f"SELECT * FROM Customer WHERE phone='{username}';"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    temp = session["user"]
                    print(temp)
                    print(temp[0])
                    return redirect(url_for("customer"))
            return  redirect(url_for("login"))
                
        elif(typeOf=="Restaurant"):
            q=f"SELECT * FROM Restaurant WHERE restaurantID='{username}';"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("restaurant"))
            return  redirect(url_for("login"))
                
        elif(typeOf=="Management"):
            q=f"SELECT * FROM Management WHERE employeeID='{username}';"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("management"))
            return  redirect(url_for("login"))

        elif(typeOf == "DeliveryWorker"):
            q=f"SELECT * FROM DeliveryWorker WHERE employeeID='{username}';"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("delivery"))
            return  redirect(url_for("login"))

        elif(typeOf == "Donor"):
            q=f"SELECT * FROM Donor WHERE donorID ='{username}';"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("donor"))
            return  redirect(url_for("login"))

        elif(typeOf == "Receiver"):
            q=f"SELECT * FROM Receiver WHERE receiverID='{username}';"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("receiver"))
            return  redirect(url_for("login"))

        else:
            return redirect(url_for("login"))
        
@app.route("/customer", methods= ["POST", "GET"])
def customer():
    if "user" in session:
        mycursor = mydb.cursor()
        mycursor.execute("Select r.name, r.description, r.city, r.type, a.av from Restaurant r, (Select restaurantID, avg(ratings) as av from Rates group by restaurantID)a where a.restaurantID = r.restaurantID;")
        myresult = mycursor.fetchall()
        return render_template("customer.html", x = myresult)
    else:
        return redirect(url_for("login"))
    

@app.route("/customer/profile")
def custprof():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select * from Customer where phone = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("customerProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))


@app.route("/customer/orders")
def pastorders():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select o.orderID, o.customerID, o.restaurantID, o.billAmt, o.tip, o.status, o.dateTime, o.paymentMode, r.name from Orders o, Restaurant r where o.restaurantID = r.restaurantID and customerID = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("customerOrders.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/management", methods= ["POST", "GET"])
def management():
    if "user" in session:
        return render_template("management.html")
    else:
        return redirect(url_for("login"))


@app.route("/management/profile")
def management_prof():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select * from Management where employeeID = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("managementProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/delivery", methods= ["POST", "GET"])
def delivery():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select o.OrderID, r.name, r.street, r.city, r.state, r.pin, c.phone, c.hNo, c.street, c.area, c.city, c.pin, o.paymentMode, o.billAmt from Orders o, Restaurant r, Customer c where c.phone = o.customerID and r.restaurantID = o.restaurantID and o.deliveryWorkerID = '{user}'")
        myresult = mycursor.fetchall()
        mycursor.execute(f"Select d.donationID, do.phone, do.hNo, do.area, do.city, do.state, do.pin, r.name, r.street, r.area, r.city, r.state, r.pin from Donation d, Donor do, Receiver r where r.receiverID = d.receiverID and d.donorID = do.donorID and d.deliveryWorkerID = '{user}'")
        myresult2 = mycursor.fetchall()
        return render_template("delivery.html", x = myresult, y = myresult2)
    else:
        return redirect(url_for("login"))
    
@app.route("/delivery/profile")
def delivery_profile():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select * from DeliveryWorker where employeeID = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("deliveryProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/donor", methods= ["POST", "GET"])
def donor():
    if "user" in session:
        mycursor = mydb.cursor()
        mycursor.execute("Select * from Receiver;")
        myresult = mycursor.fetchall()
        return render_template("donor.html", x= myresult)
    else:
        return redirect(url_for("login"))

@app.route("/donor/profile")
def donor_prof():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select * from Donor where donorID = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("donorProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/donor/donations")
def donor_donations():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select d.donationID, d.deliveryWorkerID, d.dateTime, d.category, d.status, d.quantity, r.name from Receiver r, Donation d where d.receiverID = r.receiverID and donorID = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("donorDonations.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/restaurant", methods= ["POST", "GET"])
def restaurant():
    if "user" in session:
        restaurantID = session.get("user")[0];
        q = f"SELECT name, price, discount, category, isVeg FROM food WHERE restaurantID = '{restaurantID}';"
        mycursor.execute(q)
        myresult = mycursor.fetchall()
        myresult.append(session.get("user")[3])
        return render_template("restaurant.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/receiver", methods= ["POST", "GET"])
def receiver():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select d.donationID, d.deliveryWorkerID, d.dateTime, d.category, d.status, d.quantity, r.name from Donor r, Donation d where d.donorID = r.donorID and receiverID = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("receiver.html", x= myresult)
    else:
        return redirect(url_for("login"))

@app.route("/receiver/profile")
def receiver_prof():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select * from Receiver where receiverID = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("receiverProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# To place order by customer
@app.route("/customer/place", methods= ["POST", "GET"])
def place():
    if request.method == "POST":
        user = session.get("user")[0]
        payment_mode = request.form.get("payment_mode")
        food1 = request.form.get("food1")
        food2 = request.form.get("food2")
        food3 = request.form.get("food3")

        quantity1 = request.form.get("quantity1")
        quantity2 = request.form.get("quantity2")
        quantity3 = request.form.get("quantity3")

        if (food1 != "" and quantity1 == ""):
            print("quantity1 empty")
            return redirect(url_for("place"))
        
        if (food2 != "" and quantity2 == ""):
            print("quantity2 empty")
            return redirect(url_for("place"))

        if (food3 != "" and quantity3 == ""):
            print("quantity3  empty")
            return redirect(url_for("place"))

        # check if form details are correct
        flag = False
        q=f"SELECT * FROM Customer WHERE phone='{user}';"
        print(q)
        mycursor.execute(q)
        res = mycursor.fetchall()
        # print(res)
        if(len(res) != 1):
            flag = True

        q=f"SELECT itemID FROM food;"
        print(q)
        mycursor.execute(q)
        res = mycursor.fetchall()
        if (food1 != "" and (food1,) not in res):
            flag = True
        if (food2 != "" and (food2,) not in res):
            print("food2: ",food2)
            flag = True
        if (food3 != "" and (food3,) not in res):
            print("food3: ",food3)
            flag = True

        if(flag):
            print("Invalid details")
            return  redirect(url_for("place"))

        # find the next order number
        q=f"SELECT orderID FROM orders;"
        # print(q)
        mycursor.execute(q)
        res = mycursor.fetchall()
        # print(res)
        mx = 0
        for i in res:
            if(int(i[0][1:]) > mx):
                mx = int(i[0][1:])

        next_order = 'O'+str(mx+1)

        #check if all food are from same restaurant, else give error
        q=f"SELECT itemID, restaurantID, price FROM food;"
        print(q)
        mycursor.execute(q)
        res = mycursor.fetchall()
        
        restaurant_name1 = ''
        restaurant_name2 = ''
        restaurant_name3 = ''

        bill_amount = 0

        for i in res:
            if (food1 != "" and food1 in i):
                restaurant_name1 = i[1]
                bill_amount += i[2] * int(quantity1)
            if (food2 != "" and food2 in i):
                restaurant_name2 = i[1] 
                bill_amount += i[2] * int(quantity2)
            if (food3 != "" and food3 in i):
                restaurant_name3 = i[1]
                bill_amount += i[2] * int(quantity3)



        if(food1 != "" and food2 != "" and food1 == food2):
            print("Same food names for 1 and 2,",food1)
            return redirect(url_for("place"))

        if(food2 != "" and food3 != "" and food2 == food3):
            print("Same food names for 2 and 3,",food2)
            return redirect(url_for("place"))

        if(food1 != "" and food3 != "" and food1 == food3):
            print("Same food names for 1 and 3,",food1)
            return redirect(url_for("place"))



        if(food1 != "" and food2 != "" and restaurant_name1 != restaurant_name2):
            print("Restaurant names don't match for 1 and 2")
            return redirect(url_for("place"))

        if(food1 != "" and food3 != "" and restaurant_name1 != restaurant_name3):
            print("Restaurant names don't match for 1 and 3")
            return redirect(url_for("place"))

        if(food2 != "" and food3 != "" and restaurant_name2 != restaurant_name3):
            print("Restaurant names don't match for 2 and 3")
            return redirect(url_for("place"))


        dt = datetime.now()
        dt = dt.strftime("%Y-%m-%d %H-%M-%S")

        discount_value = str(randint(1,30))

        # generate all relevant data related to the order
        q=f"INSERT INTO orders(orderID, status, dateTime, billAmt, paymentMode, customerID, restaurantID, deliveryWorkerID, discount, tip) VALUES('{next_order}', 'Active', '{dt}', {str(bill_amount)}, '{payment_mode}', '{user}', '{restaurant_name1}', 'E250{800+2*randint(0,49)}', {discount_value}, 0);"
        print(q)
        mycursor.execute(q)
        myresult = mycursor.fetchall()
        mydb.commit()
        print(myresult)

        if(food1 != ""):
            q=f"INSERT INTO contains(foodID, orderID, quantity) VALUES('{food1}', '{next_order}', {quantity1});"
            print(q)
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            mydb.commit()
            print(myresult)
        if(food2 != ""):
            q=f"INSERT INTO contains(foodID, orderID, quantity) VALUES('{food2}', '{next_order}', {quantity2});"
            print(q)
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            mydb.commit()
            print(myresult)
        if(food3 != ""):
            q=f"INSERT INTO contains(foodID, orderID, quantity) VALUES('{food3}', '{next_order}', {quantity3});"
            print(q)
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            mydb.commit()
            print(myresult)


        # Add relevant order details to `prepares`, `places`, `delivers` tables
        # But these table doesn't exist yet.


    else:
        print("The User logged in is: ",session.get("user"))

    return render_template("customerPlace.html")


# To make a donation by donor
@app.route("/donor/make", methods= ["POST", "GET"])
def make():
    if request.method == "POST":
        donorID = session.get("user")[0]
        
        category = request.form.get("category")
        quantity = request.form.get("quantity")
        
        try:
            if(int(quantity) <= 0):
                print("Cannot make donation with quantity:",quantity)
        except:
            print("Wrong Quantity Input Format")
            return redirect(url_for("make"))


        # get next DonationID
        q = f"SELECT donationID FROM donation;"
        # print(q)
        mycursor.execute(q)
        res = mycursor.fetchall()
        # print(res)
        mx = 0
        for i in res:
            if(int(i[0][2:]) > mx):
                mx = int(i[0][2:])

        donationID = "DO"+str(mx+1)

        dt = datetime.now()
        dt = dt.strftime("%Y-%m-%d %H-%M-%S")

        q = f"INSERT INTO donation(donationID, donorID, receiverID, deliveryWorkerID, dateTime, category, status, quantity) VALUES('{donationID}', '{donorID}', NULL, 'E250{800+2*randint(0,49)}', '{dt}', '{category}', 'active', {quantity});"
        print(q)
        mycursor.execute(q)
        myresult = mycursor.fetchall()
        mydb.commit()
        print(myresult)

        q = f"SELECT points FROM donor WHERE donorID = '{donorID}';"
        print(q)
        mycursor.execute(q)
        res = mycursor.fetchall()

        new_points = str((int(res[0][0]))+randint(10,50));

        q = f"UPDATE donor SET points = {new_points};"
        print(q)
        mycursor.execute(q)
        res = mycursor.fetchall()
        mydb.commit()


        # Add relevant order details to `donates` table
        # But this table doesn't exist yet.

    else:
        print("The Donor logged in is: ",session.get("user"))
    return render_template("donorMake.html")


if __name__ == "__main__":
    app.run(debug=True)
