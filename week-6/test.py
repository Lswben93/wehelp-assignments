import mysql.connector

memberDB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1015",
    database="website",
    charset='utf8'
)
ipname=input("帳號:")
ippassword=input("密碼:")
mycursor=memberDB.cursor()

mycursor.execute("SELECT name,username,password FROM member WHERE username='"+ipname+"' AND password='"+ippassword+"'")
check=mycursor.fetchone()

print(check[0])











        