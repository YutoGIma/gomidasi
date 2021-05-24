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

@app.route("/set_mail/<int:id>")
def set_mail(id):
    return render_template("set_mail.html",id=id)

@app.route("/topmenu/<int:id>/<int:user_id>")
def topmenu(id,user_id):
    conn=sqlite3.connect("ゴミ分別DB.db")
    c=conn.cursor()
    c.execute("select erea,cal from erea where id=? ",(id,))
    sel_erea=c.fetchall()
    cal=sel_erea[0][1]
    sel_erea=sel_erea[0][0]
    c.close()
    return render_template("topmenu.html",sel_erea=sel_erea,cal=cal,user_id=user_id,id=id)


@app.route("/set_mail",methods=["POST"])
def set_mail_post():
    id=request.form.get("erea_id")
    mail=request.form.get("mail_ad")
    conn=sqlite3.connect("ゴミ分別DB.db")
    c=conn.cursor()
    c.execute("insert into users values (null,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0)",(id,mail))
    conn.commit()
    c.execute("select id from users where erea_id=? and mail=?",(id,mail))
    user_id=c.fetchone()
    user_id=user_id[0]
    c.close
    return redirect("/topmenu/%s/%s"%(id,user_id))




@app.route("/bell/<int:id>/<int:user_id>")
def bell(id,user_id):
    return render_template("bell.html",id=id,user_id=user_id)

@app.route("/bell_fire_day/<int:id>/<int:user_id>")
def bell_fire_day(id,user_id):
    conn=sqlite3.connect("ゴミ分別DB.db")
    c=conn.cursor()
    c.execute("select cal from erea where id=? ",(id,))
    sce=c.fetchone()
    i=0
    belll=[]
    sce=sce[0]
    for week in sce:
        bellr=(i,week)
        belll.append(bellr)
        i+=1
    for bella in belll:
        if bella ==(0,"1"):
            c.execute("update users set 月1=1 where id=?",(user_id,))
            conn.commit()
        if bella==(1,"1"):
            c.execute("update users set 火1=1 where id=?",(user_id,))
            conn.commit()
        if bella==(2,"1"):
            c.execute("update users set 水1=1 where id=?",(user_id,))
            conn.commit()
        if bella==(3,"1"):
            c.execute("update users set 木1=1 where id=?",(user_id,))
            conn.commit()
        if bella==(4,"1"):
            c.execute("update users set 金1=1 where id=?",(user_id,))
            conn.commit()
        if bella==(5,"1"):
            c.execute("update users set 土1=1 where id=?",(user_id,))
            conn.commit()
        if bella==(6,"1"):
            c.execute("update users set 日1=1 where id=?",(user_id,))
            conn.commit()
    c.close()
    return redirect("/bell/%s/%s"%(id,user_id))

@app.route("/bell_fire_last/<int:id>/<int:user_id>")
def bell_fire_last(id,user_id):
    conn=sqlite3.connect("ゴミ分別DB.db")
    c=conn.cursor()
    c.execute("select cal from erea where id=? ",(id,))
    sce=c.fetchone()
    i=0
    belll=[]
    sce=sce[0]
    for week in sce:
        bellr=(i,week)
        belll.append(bellr)
        i+=1
    for bella in belll:
        if bella ==(0,"1"):
            c.execute("update users set 月2=1 where id=?",(user_id,))
            conn.commit()
        if bella==(1,"1"):
            c.execute("update users set 火2=1 where id=?",(user_id,))
            conn.commit()
        if bella==(2,"1"):
            c.execute("update users set 水2=1 where id=?",(user_id,))
            conn.commit()
        if bella==(3,"1"):
            c.execute("update users set 木2=1 where id=?",(user_id,))
            conn.commit()
        if bella==(4,"1"):
            c.execute("update users set 金2=1 where id=?",(user_id,))
            conn.commit()
        if bella==(5,"1"):
            c.execute("update users set 土2=1 where id=?",(user_id,))
            conn.commit()
        if bella==(6,"1"):
            c.execute("update users set 日2=1 where id=?",(user_id,))
            conn.commit()
    c.close()
    return redirect("/bell/%s/%s"%(id,user_id))

@app.route("/bell_nofire_day/<int:id>/<int:user_id>")
def bell_nofire_day(id,user_id):
    conn=sqlite3.connect("ゴミ分別DB.db")
    c=conn.cursor()
    c.execute("select cal from erea where id=? ",(id,))
    sce=c.fetchone()
    i=0
    belll=[]
    sce=sce[0]
    for week in sce:
        bellr=(i,week)
        belll.append(bellr)
        i+=1
    for bella in belll:
        if bella ==(0,"2"):
            c.execute("update users set 月1=2 where id=?",(user_id,))
            conn.commit()
        if bella==(1,"2"):
            c.execute("update users set 火1=2 where id=?",(user_id,))
            conn.commit()
        if bella==(2,"2"):
            c.execute("update users set 水1=2 where id=?",(user_id,))
            conn.commit()
        if bella==(3,"2"):
            c.execute("update users set 木1=2 where id=?",(user_id,))
            conn.commit()
        if bella==(4,"2"):
            c.execute("update users set 金1=2 where id=?",(user_id,))
            conn.commit()
        if bella==(5,"2"):
            c.execute("update users set 土1=2 where id=?",(user_id,))
            conn.commit()
        if bella==(6,"2"):
            c.execute("update users set 日1=2 where id=?",(user_id,))
            conn.commit()
    c.close()
    return redirect("/bell/%s/%s"%(id,user_id))

@app.route("/bell_nofire_last/<int:id>/<int:user_id>")
def bell_nofire_last(id,user_id):
    conn=sqlite3.connect("ゴミ分別DB.db")
    c=conn.cursor()
    c.execute("select cal from erea where id=? ",(id,))
    sce=c.fetchone()
    i=0
    belll=[]
    sce=sce[0]
    for week in sce:
        bellr=(i,week)
        belll.append(bellr)
        i+=1
    for bella in belll:
        if bella ==(0,"2"):
            c.execute("update users set 月2=2 where id=?",(user_id,))
            conn.commit()
        if bella==(1,"2"):
            c.execute("update users set 火2=2 where id=?",(user_id,))
            conn.commit()
        if bella==(2,"2"):
            c.execute("update users set 水2=2 where id=?",(user_id,))
            conn.commit()
        if bella==(3,"2"):
            c.execute("update users set 木2=2 where id=?",(user_id,))
            conn.commit()
        if bella==(4,"2"):
            c.execute("update users set 金2=2 where id=?",(user_id,))
            conn.commit()
        if bella==(5,"2"):
            c.execute("update users set 土2=2 where id=?",(user_id,))
            conn.commit()
        if bella==(6,"2"):
            c.execute("update users set 日2=2 where id=?",(user_id,))
            conn.commit()
    c.close()
    return redirect("/bell/%s/%s"%(id,user_id))

@app.route("/bell_source_day/<int:id>/<int:user_id>")
def bell_source_day(id,user_id):
    conn=sqlite3.connect("ゴミ分別DB.db")
    c=conn.cursor()
    c.execute("select cal from erea where id=? ",(id,))
    sce=c.fetchone()
    i=0
    belll=[]
    sce=sce[0]
    for week in sce:
        bellr=(i,week)
        belll.append(bellr)
        i+=1
    for bella in belll:
        if bella ==(0,"3"):
            c.execute("update users set 月1=3 where id=?",(user_id,))
            conn.commit()
        if bella==(1,"3"):
            c.execute("update users set 火1=3 where id=?",(user_id,))
            conn.commit()
        if bella==(2,"3"):
            c.execute("update users set 水1=3 where id=?",(user_id,))
            conn.commit()
        if bella==(3,"3"):
            c.execute("update users set 木1=3 where id=?",(user_id,))
            conn.commit()
        if bella==(4,"3"):
            c.execute("update users set 金1=3 where id=?",(user_id,))
            conn.commit()
        if bella==(5,"3"):
            c.execute("update users set 土1=3 where id=?",(user_id,))
            conn.commit()
        if bella==(6,"3"):
            c.execute("update users set 日1=3 where id=?",(user_id,))
            conn.commit()
    c.close()
    return redirect("/bell/%s/%s"%(id,user_id))

@app.route("/bell_source_last/<int:id>/<int:user_id>")
def bell_source_last(id,user_id):
    conn=sqlite3.connect("ゴミ分別DB.db")
    c=conn.cursor()
    c.execute("select cal from erea where id=? ",(id,))
    sce=c.fetchone()
    i=0
    belll=[]
    sce=sce[0]
    for week in sce:
        bellr=(i,week)
        belll.append(bellr)
        i+=1
    for bella in belll:
        if bella ==(0,"3"):
            c.execute("update users set 月2=3 where id=?",(user_id,))
            conn.commit()
        if bella==(1,"3"):
            c.execute("update users set 火2=3 where id=?",(user_id,))
            conn.commit()
        if bella==(2,"3"):
            c.execute("update users set 水2=3 where id=?",(user_id,))
            conn.commit()
        if bella==(3,"3"):
            c.execute("update users set 木2=3 where id=?",(user_id,))
            conn.commit()
        if bella==(4,"3"):
            c.execute("update users set 金2=3 where id=?",(user_id,))
            conn.commit()
        if bella==(5,"3"):
            c.execute("update users set 土2=3 where id=?",(user_id,))
            conn.commit()
        if bella==(6,"3"):
            c.execute("update users set 日2=3 where id=?",(user_id,))
            conn.commit()
    c.close()
    return redirect("/bell/%s/%s"%(id,user_id))


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