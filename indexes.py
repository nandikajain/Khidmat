import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="nandikajain",passwd="3827" ,database = "khidmatDB")

mycursor = mydb.cursor()
query="SHOW INDEX FROM khidmatDB.Contains;"
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Contains: ')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM khidmatDB.Customer; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Customer:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM khidmatDB.DeliveryWorker; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for DeliveryWorker:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM khidmatDB.Donation; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Donation:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM khidmatDB.Donor; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Donor:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM khidmatDB.Food; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Food:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM khidmatDB.Management; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Management:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM khidmatDB.Orders; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Orders:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM khidmatDB.Rates; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Rates:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM khidmatDB.Receiver; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Receiver:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM khidmatDB.Restaurant; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Restaurant:')
for x in myresult:
   print(x)