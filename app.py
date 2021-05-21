import sqlite3
from flask import Flask,render_template,request,redirect

app=Flask(__name__)

@app.route("/select_city")
def select_city():
    conn=sqlite3.connect("ゴミ分別DB.db")
    c=conn.cursor()
    c.execute("select id,city from city ")
    city=[]
    for row in c.fetchall():
        city.append({"id":row[0],"city":row[1]})
    c.close()
    return render_template("select_city.html",city=city)

@app.route("/select_city",methods=["POST"])
def city_sc():
    citysc=request.form.get("city_sc")
    citysc="%"+citysc+"%"
    conn=sqlite3.connect("ゴミ分別DB.db")
    c=conn.cursor()
    c.execute("select id,city from city where city like ?",(citysc,))
    city=[]
    for row in c.fetchall():
        city.append({"id":row[0],"city":row[1]})
    c.close()
    return render_template("select_city.html",city=city)


@app.route("/erea/<int:id>")
def erea(id):
    conn = sqlite3.connect('ゴミ分別DB.db')
    c = conn.cursor()
    c.execute("select id,erea from erea where city_id = ?", (id,) )
    erea=[]
    for row in c.fetchall():
        erea.append({"id":row[0],"erea":row[1]})
    c.close()
    return render_template("erea.html",erea=erea,id=id)

@app.route("/erea",methods=["POST"])
def erea_sc():
    id=request.form.get("erea_id")
    ereasc=request.form.get("erea_sc")
    ereasc="%"+ereasc+"%"
    conn=sqlite3.connect("ゴミ分別DB.db")
    c=conn.cursor()
    c.execute("select id,erea from erea where city_id=? and erea like ?",(id,ereasc,))
    erea=[]
    for row in c.fetchall():
        erea.append({"id":row[0],"erea":row[1]})
    c.close()
    return render_template("erea.html",erea=erea)

@app.route("/topmenu")
def topmenu():
    return render_template("topmenu.html")

@app.route("/bell")
def bell():
    return render_template("bell.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == '__main__':
    app.debug = True
    app.run()