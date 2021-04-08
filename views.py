
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="nandikajain",passwd="3827" ,database = "khidmatDB")

mycursor = mydb.cursor()
query="SHOW FULL TABLES IN khidmatDB WHERE TABLE_TYPE LIKE 'VIEW';"
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Views are')
for x in myresult:
   print(x)
print()

