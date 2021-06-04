import mysql.connector
conn = mysql.connector.connect(host="localhost",database="Mydb", user="root",password="Honey@7*")

if conn.is_connected():
    print("Connected to Mysql")

cursor = conn.cursor()
cursor.execute("select * from emp")

#using fetch one
# row = cursor.fetchone()
# while row is not None:
#     print(row)
#     row=cursor.fetchone()

#using fetchall

rows = cursor.fetchall()
for row in rows:
    print(row)
    

cursor.close()
conn.close


conn.close()