from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
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
                    return  redirect(url_for("receiever"))
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

@app.route("/delivery", methods= ["POST", "GET"])
def delivery():
    if "user" in session:
        return render_template("delivery.html")
    else:
        return redirect(url_for("login"))
        
@app.route("/donor", methods= ["POST", "GET"])
def donor():
    if "user" in session:
        return render_template("donor.html")
    else:
        return redirect(url_for("login"))

@app.route("/restaurant", methods= ["POST", "GET"])
def restaurant():
    if "user" in session:
        return render_template("restaurant.html")
    else:
        return redirect(url_for("login"))

@app.route("/receiver", methods= ["POST", "GET"])
def receiver():
    if "user" in session:
        return render_template("receiver.html")
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
    
if __name__ == "__main__":
    app.run(debug=True)
