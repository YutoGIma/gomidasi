import sqlite3
from flask import Flask,render_template,request,redirect,session


app=Flask(__name__)
app.secret_key="sunabacokoza"

@app.route("/select_city")
def select_city():
    if "user_id" in session:
        id=session.get("id")
        user_id=session.get("user_id")
        return redirect("/topmenu/%s/%s"%(id,user_id))
    else:
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
    if "user_id" in session:
        id=session.get("id")
        user_id=session.get("user_id")
        return redirect("/topmenu/%s/%s"%(id,user_id))
    else:
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
    if "user_id" in session:
        id=session.get("id")
        user_id=session.get("user_id")
        return redirect("/topmenu/%s/%s"%(id,user_id))
    else:
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
    if "user_id" in session:
        id=session.get("id")
        user_id=session.get("user_id")
        return redirect("/topmenu/%s/%s"%(id,user_id))
    else:
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

@app.route("/set_mail/<int:id>")
def set_mail(id):
    if "user_id" in session:
        id=session.get("id")
        user_id=session.get("user_id")
        return redirect("/topmenu/%s/%s"%(id,user_id))
    else:
        return render_template("set_mail.html",id=id)

@app.route("/topmenu/<int:id>/<int:user_id>")
def topmenu(id,user_id):
    if "user_id" in session:
        conn=sqlite3.connect("ゴミ分別DB.db")
        c=conn.cursor()
        c.execute("select erea,cal from erea where id=? ",(id,))
        sel_erea=c.fetchall()
        cal=sel_erea[0][1]
        sel_erea=sel_erea[0][0]
        c.close()
        return render_template("topmenu.html",sel_erea=sel_erea,cal=cal,user_id=user_id,id=id)
    else:
        return redirect("/select_city")

@app.route("/set_mail",methods=["POST"])
def set_mail_post():
    if "user_id" in session:
        id=session.get("id")
        user_id=session.get("user_id")
        return redirect("/topmenu/%s/%s"%(id,user_id))
    else:
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
        session["user_id"]=user_id
        session["id"]=id
        return redirect("/topmenu/%s/%s"%(id,user_id))

@app.route("/bell/<int:id>/<int:user_id>")
def bell(id,user_id):
    if "user_id" in session:
        conn=sqlite3.connect("ゴミ分別DB.db")
        c=conn.cursor()
        c.execute("select 月1,月2,火1,火2,水1,水2,木1,木2,金1,金2,土1,土2,日1,日2 from users where id=? ",(user_id,))
        my_bells=c.fetchall()
        my_bell=my_bells[0]
        my_bell1=[my_bell[0],my_bell[2],my_bell[4],my_bell[6],my_bell[8],my_bell[10],my_bell[12]]
        my_bell2=[my_bell[1],my_bell[3],my_bell[5],my_bell[7],my_bell[9],my_bell[11],my_bell[13]]
        fireto=no_fireto=sourceto=fireyes=no_fireyes=sourceyes=0
        for item in my_bell1:
            if item==1:
                fireto += 1
            elif item==2:
                no_fireto += 1
            elif item==3:
                sourceto += 1
        for item in my_bell2:
            if item==1:
                fireyes += 1
            elif item==2:
                no_fireyes += 1
            elif item==3:
                sourceyes += 1
        return render_template("bell.html",id=id,user_id=user_id,fireto=fireto,no_fireto=no_fireto,sourceto=sourceto,fireyes=fireyes,no_fireyes=no_fireyes,sourceyes=sourceyes)
    else:
        return redirect("/select_city")

@app.route("/reset/<int:user_id>")
def reset_bell(user_id):
    if "user_id" in session:
        conn=sqlite3.connect("ゴミ分別DB.db")
        c=conn.cursor()
        c.execute("update users set 月1=0,火1=0,水1=0,木1=0,金1=0,土1=0,日1=0,月2=0,火2=0,水2=0,木2=0,金2=0,土2=0,日2=0 where id=?",(user_id,))
        conn.commit()
        c.close
        id=session.get("id")
        return redirect("/bell/%s/%s"%(id,user_id))
    else:
        return redirect("/select_city")


@app.route("/bell_fire_day/<int:id>/<int:user_id>")
def bell_fire_day(id,user_id):
    if "user_id" in session:
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
    else:
        return redirect("/select_city")

@app.route("/bell_fire_last/<int:id>/<int:user_id>")
def bell_fire_last(id,user_id):
    if "user_id" in session:
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
    else:
        return redirect("/select_city")

@app.route("/bell_nofire_day/<int:id>/<int:user_id>")
def bell_nofire_day(id,user_id):
    if "user_id" in session:
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
    else:
        return redirect("/select_city")

@app.route("/bell_nofire_last/<int:id>/<int:user_id>")
def bell_nofire_last(id,user_id):
    if "user_id" in session:
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
    else:
        return redirect("/select_city")

@app.route("/bell_source_day/<int:id>/<int:user_id>")
def bell_source_day(id,user_id):
    if "user_id" in session:
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
    else:
        return redirect("/select_city")

@app.route("/bell_source_last/<int:id>/<int:user_id>")
def bell_source_last(id,user_id):
    if "user_id" in session:
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
    else:
        return redirect("/select_city")


@app.route("/contact")
def contact():
    if "user_id" in session:
        return render_template("contact.html")
    else:
        return redirect("/select_city")

@app.route("/del_select")
def del_select():
    if "user_id" in session:
        user_id=session.get("user_id")
        conn=sqlite3.connect("ゴミ分別DB.db")
        c=conn.cursor()
        c.execute("delete from users where id=?",(user_id,))
        conn.commit()
        c.close
        session.pop("user_id",None)
        session.pop("id",None)
        return redirect("/select_city")
    else:
        return redirect("/select_city")

@app.route("/page5/<int:id>/<int:user_id>")
def page5(id,user_id):
    if "user_id" in session:
        return render_template ("page5.html",id=id,user_id=user_id)
    else:
        return redirect("/select_city")

@app.route("/gomi_sc",methods=["POST"])
def gomi_sc():
    if "user_id" in session:
        texta=request.form.get("gomi_in")
        text="%"+texta+"%"
        conn=sqlite3.connect("okinawashidatebase.db")
        c=conn.cursor()
        c.execute("select name,type,message from gomi where name like ?",(text,))
        scresult=[]
        for row in c.fetchall():
            scresult.append({"name":row[0],"type":row[1],"message":row[2]})
        c.close()
        id=session.get("id")
        user_id=session.get("user_id")
        if scresult == []:
            return render_template("contact.html",text=texta,id=id,user_id=user_id)
        else:
            return render_template("page6.html",scresult=scresult,id=id,user_id=user_id)
    else:
        return redirect("/select_city")
    


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')