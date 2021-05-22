import sqlite3
from flask import Flask,render_template,request,redirect,session
from email.mime.text import MIMEText
import smtplib
import schedule
import datetime
import time

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


# 以下メール送信のためのコード

conn=sqlite3.connect("ゴミ分別DB.db")
c=conn.cursor()
c.execute("select mail from users where 月1=1")
users_monday_fire=[]
users_monday_fire=c.fetchall()
c.execute("select mail from users where 火1=1")
users_tueday_fire=[]
users_tueday_fire=c.fetchall()
c.execute("select mail from users where 水1=1")
users_wedday_fire=[]
users_wedday_fire=c.fetchall()
c.execute("select mail from users where 木1=1")
users_thuday_fire=[]
users_thuday_fire=c.fetchall()
c.execute("select mail from users where 金1=1")
users_friday_fire=[]
users_friday_fire=c.fetchall()
c.execute("select mail from users where 土1=1")
users_satday_fire=[]
users_satday_fire=c.fetchall()
c.execute("select mail from users where 日1=1")
users_sunday_fire=[]
users_sunday_fire=c.fetchall()
c.execute("select mail from users where 月2=1")
users_monlast_fire=[]
users_monlast_fire=c.fetchall()
c.execute("select mail from users where 火2=1")
users_tuelast_fire=[]
users_tuelast_fire=c.fetchall()
c.execute("select mail from users where 水2=1")
users_wedlast_fire=[]
users_wedlast_fire=c.fetchall()
c.execute("select mail from users where 木2=1")
users_thulast_fire=[]
users_thulast_fire=c.fetchall()
c.execute("select mail from users where 金2=1")
users_frilast_fire=[]
users_frilast_fire=c.fetchall()
c.execute("select mail from users where 土2=1")
users_satlast_fire=[]
users_satlast_fire=c.fetchall()
c.execute("select mail from users where 日2=1")
users_sunlast_fire=[]
users_sunlast_fire=c.fetchall()
c.execute("select mail from users where 月1=2")
users_monday_nofire=[]
users_monday_nofire=c.fetchall()
c.execute("select mail from users where 火1=2")
users_tueday_nofire=[]
users_tueday_nofire=c.fetchall()
c.execute("select mail from users where 水1=2")
users_wedday_nofire=[]
users_wedday_nofire=c.fetchall()
c.execute("select mail from users where 木1=2")
users_thuday_nofire=[]
users_thuday_nofire=c.fetchall()
c.execute("select mail from users where 金1=2")
users_friday_nofire=[]
users_friday_nofire=c.fetchall()
c.execute("select mail from users where 土1=2")
users_satday_nofire=[]
users_satday_nofire=c.fetchall()
c.execute("select mail from users where 日1=2")
users_sunday_nofire=[]
users_sunday_nofire=c.fetchall()
c.execute("select mail from users where 月2=2")
users_monlast_nofire=[]
users_monlast_nofire=c.fetchall()
c.execute("select mail from users where 火2=2")
users_tuelast_nofire=[]
users_tuelast_nofire=c.fetchall()
c.execute("select mail from users where 水2=2")
users_wedlast_nofire=[]
users_wedlast_nofire=c.fetchall()
c.execute("select mail from users where 木2=2")
users_thulast_nofire=[]
users_thulast_nofire=c.fetchall()
c.execute("select mail from users where 金2=2")
users_frilast_nofire=[]
users_frilast_nofire=c.fetchall()
c.execute("select mail from users where 土2=2")
users_satlast_nofire=[]
users_satlast_nofire=c.fetchall()
c.execute("select mail from users where 日2=2")
users_sunlast_nofire=[]
users_sunlast_nofire=c.fetchall()
c.execute("select mail from users where 月1=3")
users_monday_source=[]
users_monday_source=c.fetchall()
c.execute("select mail from users where 火1=3")
users_tueday_source=[]
users_tueday_source=c.fetchall()
c.execute("select mail from users where 水1=3")
users_wedday_source=[]
users_wedday_source=c.fetchall()
c.execute("select mail from users where 木1=3")
users_thuday_source=[]
users_thuday_source=c.fetchall()
c.execute("select mail from users where 金1=3")
users_friday_source=[]
users_friday_source=c.fetchall()
c.execute("select mail from users where 土1=3")
users_satday_source=[]
users_satday_source=c.fetchall()
c.execute("select mail from users where 日1=3")
users_sunday_source=[]
users_sunday_source=c.fetchall()
c.execute("select mail from users where 月2=3")
users_monlast_source=[]
users_monlast_source=c.fetchall()
c.execute("select mail from users where 火2=3")
users_tuelast_source=[]
users_tuelast_source=c.fetchall()
c.execute("select mail from users where 水2=3")
users_wedlast_source=[]
users_wedlast_source=c.fetchall()
c.execute("select mail from users where 木2=3")
users_thulast_source=[]
users_thulast_source=c.fetchall()
c.execute("select mail from users where 金2=3")
users_frilast_source=[]
users_frilast_source=c.fetchall()
c.execute("select mail from users where 土2=3")
users_satlast_source=[]
users_satlast_source=c.fetchall()
c.execute("select mail from users where 日2=3")
users_sunlast_source=[]
users_sunlast_source=c.fetchall()
c.close()


def job_fire_day(users):
# SMTP認証情報
    for user in users:
        account = "gomibacosunabaco@gmail.com"
        password = "sunabaco5344"
        
        # 送受信先
        to_email = user[0]
        from_email = "gomibacosunabaco@gmail.com"
        
        # MIMEの作成
        subject = "今日は燃えるゴミの日です。"
        message = "8時までにゴミを出しましょう。"
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email
        
        # メール送信処理
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(account, password)
        server.send_message(msg)
        server.quit()

def job_fire_last(users):
# SMTP認証情報
    for user in users:
        account = "gomibacosunabaco@gmail.com"
        password = "sunabaco5344"
        
        # 送受信先
        to_email = user[0]
        from_email = "gomibacosunabaco@gmail.com"
        
        # MIMEの作成
        subject = "明日は燃えるゴミの日です。"
        message = "8時までにゴミを出しましょう。"
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email
        
        # メール送信処理
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(account, password)
        server.send_message(msg)
        server.quit()


def job_nofire_day(users):
# SMTP認証情報
    for user in users:
        account = "gomibacosunabaco@gmail.com"
        password = "sunabaco5344"
        
        # 送受信先
        to_email = user[0]
        from_email = "gomibacosunabaco@gmail.com"
        
        # MIMEの作成
        subject = "今日は燃えないゴミの日です。"
        message = "8時までにゴミを出しましょう。"
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email
        
        # メール送信処理
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(account, password)
        server.send_message(msg)
        server.quit()

def job_nofire_last(users):
# SMTP認証情報
    for user in users:
        account = "gomibacosunabaco@gmail.com"
        password = "sunabaco5344"
        
        # 送受信先
        to_email = user[0]
        from_email = "gomibacosunabaco@gmail.com"
        
        # MIMEの作成
        subject = "明日は燃えないゴミの日です。"
        message = "8時までにゴミを出しましょう。"
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email
        
        # メール送信処理
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(account, password)
        server.send_message(msg)
        server.quit()

def job_source_day(users):
# SMTP認証情報
    for user in users:
        account = "gomibacosunabaco@gmail.com"
        password = "sunabaco5344"
        
        # 送受信先
        to_email = user[0]
        from_email = "gomibacosunabaco@gmail.com"
        
        # MIMEの作成
        subject = "今日は資源ゴミの日です。"
        message = "8時までにゴミを出しましょう。"
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email
        
        # メール送信処理
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(account, password)
        server.send_message(msg)
        server.quit()

def job_source_last(users):
# SMTP認証情報
    for user in users:
        account = "gomibacosunabaco@gmail.com"
        password = "sunabaco5344"
        
        # 送受信先
        to_email = user[0]
        from_email = "gomibacosunabaco@gmail.com"
        
        # MIMEの作成
        subject = "明日は資源ゴミの日です。"
        message = "8時までにゴミを出しましょう。"
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email
        
        # メール送信処理
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(account, password)
        server.send_message(msg)
        server.quit()

schedule.every().monday.at("07:00").do(job_fire_day,users=users_monday_fire)
schedule.every().monday.at("07:00").do(job_nofire_day,users=users_monday_nofire)
schedule.every().monday.at("07:00").do(job_source_day,users=users_monday_source)
schedule.every().tuesday.at("07:00").do(job_fire_day,users=users_tueday_fire)
schedule.every().tuesday.at("07:00").do(job_nofire_day,users=users_tueday_nofire)
schedule.every().tuesday.at("07:00").do(job_source_day,users=users_tueday_source)
schedule.every().wednesday.at("07:00").do(job_fire_day,users=users_wedday_fire)
schedule.every().wednesday.at("07:00").do(job_nofire_day,users=users_wedday_nofire)
schedule.every().wednesday.at("07:00").do(job_source_day,users=users_wedday_source)
schedule.every().thursday.at("07:00").do(job_fire_day,users=users_thuday_fire)
schedule.every().thursday.at("07:00").do(job_nofire_day,users=users_thuday_nofire)
schedule.every().thursday.at("07:00").do(job_source_day,users=users_thuday_source)
schedule.every().friday.at("07:00").do(job_fire_day,users=users_friday_fire)
schedule.every().friday.at("07:00").do(job_nofire_day,users=users_friday_nofire)
schedule.every().friday.at("07:00").do(job_source_day,users=users_friday_source)
schedule.every().saturday.at("07:00").do(job_fire_day,users=users_satday_fire)
schedule.every().saturday.at("07:00").do(job_nofire_day,users=users_satday_nofire)
schedule.every().saturday.at("07:00").do(job_source_day,users=users_satday_source)
schedule.every().sunday.at("07:00").do(job_fire_day,users=users_sunday_fire)
schedule.every().sunday.at("07:00").do(job_nofire_day,users=users_sunday_nofire)
schedule.every().sunday.at("07:00").do(job_source_day,users=users_sunday_source)
schedule.every().sunday.at("20:00").do(job_fire_last,users=users_monlast_fire)
schedule.every().sunday.at("20:00").do(job_nofire_last,users=users_monlast_nofire)
schedule.every().sunday.at("20:00").do(job_source_last,users=users_monlast_source)
schedule.every().wednesday.at("20:00").do(job_fire_last,users=users_tuelast_fire)
schedule.every().wednesday.at("20:00").do(job_nofire_last,users=users_tuelast_nofire)
schedule.every().wednesday.at("20:00").do(job_source_last,users=users_tuelast_source)
schedule.every().thursday.at("20:00").do(job_fire_last,users=users_wedlast_fire)
schedule.every().thursday.at("20:00").do(job_nofire_last,users=users_wedlast_nofire)
schedule.every().thursday.at("20:00").do(job_source_last,users=users_wedlast_source)
schedule.every().friday.at("20:00").do(job_fire_last,users=users_thulast_fire)
schedule.every().friday.at("20:00").do(job_nofire_last,users=users_thulast_nofire)
schedule.every().friday.at("20:00").do(job_source_last,users=users_thulast_source)
schedule.every().saturday.at("20:00").do(job_fire_last,users=users_frilast_fire)
schedule.every().saturday.at("20:00").do(job_nofire_last,users=users_frilast_nofire)
schedule.every().saturday.at("20:00").do(job_source_last,users=users_frilast_source)
schedule.every().sunday.at("20:00").do(job_fire_last,users=users_satlast_fire)
schedule.every().sunday.at("20:00").do(job_nofire_last,users=users_satlast_nofire)
schedule.every().sunday.at("20:00").do(job_source_last,users=users_satlast_source)
schedule.every().monday.at("20:00").do(job_fire_last,users=users_sunlast_fire)
schedule.every().monday.at("20:00").do(job_nofire_last,users=users_sunlast_nofire)
schedule.every().monday.at("20:00").do(job_source_last,users=users_sunlast_source)

schedule.run_pending()
if __name__ == '__main__':
    app.debug = True
    app.run()