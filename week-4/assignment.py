from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import url_for
from flask import redirect

app=Flask(__name__)

app.secret_key="topSecret"

@app.route("/",methods=["GET","POST"])
def index():
    return  render_template("homepage.html")

@app.route("/signin",methods=["POST","GET"])
def signin():
        account=request.form["account"]
        password=request.form["password"]
        if account=="test" and password=="test":
            session["username"]=account
            return redirect(url_for("member"))
        elif account=="" or password=="":
            return redirect(url_for("error",message=["enter"]))
        else:
            return redirect(url_for("error",message=["error"]))

@app.route("/member/",methods=["GET"])
def member():
    if "username" in session:
        return render_template("member.html")
    else:
        return  render_template("homepage.html")

@app.route("/error/",methods=["GET"])
def error():
    keyword=request.args.get("message","error")
    if keyword=="error":
        return  render_template("error.html")
    else:
        return  render_template("enter.html")

@app.route("/signout",methods=["GET"])
def signout():
    session.pop("username", None)
    return  redirect("/")


app.run(port=3000)

#待解決問題
#1.使用者必須登入才能看到使用者頁面
#2.session紀錄