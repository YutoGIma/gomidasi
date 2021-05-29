import sqlite3
from flask import Flask
from email.mime.text import MIMEText
import smtplib
import schedule
import datetime
import time


app=Flask(__name__)
app.secret_key="sunabacokoza"


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
schedule.every().monday.at("20:00").do(job_fire_last,users=users_tuelast_fire)
schedule.every().monday.at("20:00").do(job_nofire_last,users=users_tuelast_nofire)
schedule.every().monday.at("20:00").do(job_source_last,users=users_tuelast_source)
schedule.every().tuesday.at("20:00").do(job_fire_last,users=users_wedlast_fire)
schedule.every().tuesday.at("20:00").do(job_nofire_last,users=users_wedlast_nofire)
schedule.every().tuesday.at("20:00").do(job_source_last,users=users_wedlast_source)
schedule.every().wednesday.at("20:00").do(job_fire_last,users=users_thulast_fire)
schedule.every().wednesday.at("20:00").do(job_nofire_last,users=users_thulast_nofire)
schedule.every().wednesday.at("20:00").do(job_source_last,users=users_thulast_source)
schedule.every().thursday.at("20:00").do(job_fire_last,users=users_frilast_fire)
schedule.every().thursday.at("20:00").do(job_nofire_last,users=users_frilast_nofire)
schedule.every().thursday.at("20:00").do(job_source_last,users=users_frilast_source)
schedule.every().friday.at("20:00").do(job_fire_last,users=users_satlast_fire)
schedule.every().friday.at("20:00").do(job_nofire_last,users=users_satlast_nofire)
schedule.every().friday.at("20:00").do(job_source_last,users=users_satlast_source)
schedule.every().saturday.at("20:00").do(job_fire_last,users=users_sunlast_fire)
schedule.every().saturday.at("20:00").do(job_nofire_last,users=users_sunlast_nofire)
schedule.every().saturday.at("20:00").do(job_source_last,users=users_sunlast_source)

while True:
  schedule.run_pending()
  time.sleep(1)