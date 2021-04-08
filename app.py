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
            print(q)
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            print(myresult)
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return redirect(url_for("customer"))
            return  redirect(url_for("login"))
                
        elif(typeOf=="Restaurant"):
            q=f"SELECT * FROM Restaurant WHERE restaurantID='{username}';"
            print(q)
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            print(myresult)
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("restaurant"))
            return  redirect(url_for("login"))
                
        elif(typeOf=="Management"):
            q=f"SELECT * FROM Management WHERE employeeID='{username}';"
            print(q)
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            print(myresult)
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("management"))
            return  redirect(url_for("login"))

        elif(typeOf == "DeliveryWorker"):
            q=f"SELECT * FROM DeliveryWorker WHERE employeeID='{username}';"
            print(q)
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            print(myresult)
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("delivery"))
            return  redirect(url_for("login"))

        elif(typeOf == "Donor"):
            q=f"SELECT * FROM Donor WHERE donorID ='{username}';"
            print(q)
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            print(myresult)
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("donor"))
            return  redirect(url_for("login"))

        elif(typeOf == "Receiver"):
            q=f"SELECT * FROM Receiver WHERE receiverID='{username}';"
            print(q)
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            print(myresult)
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
    return render_template("customer.html")

@app.route("/management", methods= ["POST", "GET"])
def management():
    return render_template("management.html")

@app.route("/delivery", methods= ["POST", "GET"])
def delivery():
    return render_template("delivery.html")

@app.route("/donor", methods= ["POST", "GET"])
def donor():
    return render_template("donor.html")

@app.route("/restaurant", methods= ["POST", "GET"])
def restaurant():
    return render_template("restaurant.html")

@app.route("/receiver", methods= ["POST", "GET"])
def receiver():
    return render_template("receiver.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
    
if __name__ == "__main__":
    app.run(debug=True)
