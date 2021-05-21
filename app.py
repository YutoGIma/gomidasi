import sqlite3
from flask import Flask,render_template,request,redirect,session

app=Flask(__name__)
app.secret_key="sunabacokoza"

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
    session["erea_id"]=erea["id"]
    return render_template("erea.html",erea=erea)

@app.route("/topmenu/<int:id>")
def topmenu(id):
    conn=sqlite3.connect("ゴミ分別DB.db")
    c=conn.cursor()
    c.execute("insert into users values (null,?,null,0,0,0,0,0,0,0,0,0,0,0,0,0,0)",(id,))
    conn.commit()
    c.execute("select erea,cal from erea where id=? ",(id,))
    sel_erea=c.fetchall()
    cal=sel_erea[0][1]
    sel_erea=sel_erea[0][0]
    c.close()
    return render_template("topmenu.html",sel_erea=sel_erea,cal=cal)

@app.route("/bell")
def bell():
    return render_template("bell.html")

@app.route("/bell_fire_day")
def bell_fire_day():
    return redirect("/bell")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/del_select")
def del_select():
    session.pop("erea_id",None)
    return redirect("/select_city")



if __name__ == '__main__':
    app.debug = True
    app.run()