from flask import Flask
from flask import make_response, render_template
import json
import sqlite3

app= Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/shops')
def shops():
    response = make_response(render_template('shops.json'))
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return response


@app.route('/mr4')
def mr4():
    con = sqlite3.connect('sensor.db')
    cur = con.cursor()
    cur.execute('select * from data ORDER BY id DESC limit 10')
    rows = cur.fetchall()

    l = list()
    for r in rows:
        d = dict()
        d['id'] = r[0]
        d['nowDate'] = r[1]
        d['nowTime'] = r[2]
        d['humidity'] = round(float(r[3]),2)
        d['temperature'] = round(float(r[4]),2)
        l.append(d)

    jsonD = json.dumps(l)
    con.close()
    response = make_response(jsonD)
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return response

