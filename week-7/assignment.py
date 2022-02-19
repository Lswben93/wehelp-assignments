from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import url_for
from flask import redirect
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

memberDB=mysql.connector.connect(
    host=os.getenv("host"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database"),
    charset='utf8'
)

app=Flask(__name__)

app.secret_key="topSecret"

@app.route("/",methods=["GET","POST"])
def index():
    return  render_template("homepage.html")

@app.route("/signin",methods=["POST","GET"])
def signin():
    signName=request.form["signName"]
    signAccount=request.form["signAccount"]
    signPassword=request.form["signPassword"]
    if signName=="" or signAccount=="" or signPassword=="":
        return redirect(url_for("error",message=["signEnter"]))
    else:
        mycursor=memberDB.cursor()
        mycursor.execute("SELECT username FROM member WHERE username=%s",(signAccount,))
        check=mycursor.fetchone()
        if check==None:
            query="INSERT INTO member(name,username,password) VALUES(%s,%s,%s)"
            mycursor.execute(query,(signName,signAccount,signPassword))
            return render_template("homepage.html")
        else:
            return redirect(url_for("error",message=["exist"]))

@app.route("/login",methods=["POST","GET"])
def login():
        mycursor=memberDB.cursor()
        account=request.form["account"]
        password=request.form["password"]
        mycursor.execute("SELECT name,username,password FROM member WHERE username=%s AND password=%s",(account,password,))
        newcursor=mycursor.fetchone()
        if newcursor!=None:
            session["username"]=account
            return redirect(url_for("member"))
        elif account=="" or password=="":
            return redirect(url_for("error",message=["enter"]))
        else:
            return redirect(url_for("error",message=["error"]))

@app.route("/member/",methods=["GET"])
def member():
    if "username" in session:
        mycursor=memberDB.cursor()
        mycursor.execute("SELECT name,username FROM member where username='"+session["username"]+"'")
        newcursor=mycursor.fetchone()
        return render_template("member.html",name=newcursor[0])
    else:
        return  render_template("homepage.html")

@app.route("/error/",methods=["GET"])
def error():
    keyword=request.args.get["message"]
    if keyword=="error":
        message="帳號或密碼輸入錯誤"
        return  render_template("error.html", message=message)
    elif keyword=="enter":
        message="請輸入帳號密碼"
        return  render_template("error.html", message=message)
    elif keyword=="exist":
        message="帳號已經被註冊"
        return  render_template("error.html", message=message)
    else:
        message="請輸入姓名、帳號或密碼"
        return  render_template("error.html", message=message)
    

@app.route("/signout",methods=["GET"])
def signout():
    session.pop("username", None)
    return  redirect("/")

@app.route("/api/members",methods=["GET"])
def api():
    username=request.args.get("username")
    mycursor=memberDB.cursor(dictionary=True)
    mycursor.execute("SELECT id, name, username FROM member WHERE username=%s",(username,))
    result=mycursor.fetchone()
    return {"data":result}
    

app.run(port=3000)

