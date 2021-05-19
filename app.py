import sqlite3
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/select_city")
def select_city():
    return render_template("select_city.html")




if __name__ == '__main__':
    app.debug = True
    app.run()