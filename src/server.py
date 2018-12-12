import os
import json
import ConfigParser
import campus_questions
import events_questions
from flaskext.mysql import MySQL
from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin
from uuid import uuid4


app = Flask(__name__)
mysql = MySQL()
config = ConfigParser.ConfigParser()
config.read('config.cfg')
app.config['MYSQL_DATABASE_HOST'] = config.get('MySQL', 'host') 
app.config['MYSQL_DATABASE_DB'] = config.get('MySQL', 'db')
app.config['MYSQL_DATABASE_USER'] = config.get('MySQL', 'user') 
app.config['MYSQL_DATABASE_PASSWORD'] = config.get('MySQL', 'passwd') 
mysql.init_app(app)
CORS(app)

## post del bot
@app.route('/bot', methods=['POST'])
def post_bot():
    content = request.get_json(silent=True)
    mail = content['email']
    date = content['date']
    #Es la acción
    type = content['type']
    mode = content['mode']
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        cursor.execute('insert into BOT values(null, %s, %s, %s, %s)', (mail, date,type, mode))
        conn.commit()
    except:
        conn.rollback()
        return json.dumps({'status':'error'}), 505
    return json.dumps({'status':'succes'}), 200

## get del bot
def get_bot():
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        cursor.execute('select * from BOT')
        lista = [{'id':campus_id,'email':email,'date':date, 'type':tipo, 'mode': modo} for (campus_id, email, date,tipo, modo) in cursor]
        conn.close()
        return lista
    except:
        conn.close()
        return []

# question 1
@app.route('/bot/<question_number>', methods=['GET'])
def get_bot_questions(question_number):
    bot_data = get_bot()
    data = bot_questions.resolve_question(int(question_number)-1, bot_data)
    return json.dumps({'status':'success', 'data': data})

## post del campus
@app.route('/campus', methods=['POST'])
def post_campus():
    content = request.get_json(silent=True)
    mail = content['email']
    date = content['date']
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        cursor.execute('insert into CAMPUS values(null, %s, %s)', (mail, date))
        conn.commit()
    except:
        conn.rollback()
        return json.dumps({'status':'error'}), 505
    return json.dumps({'status':'succes'}), 200

## get del campus
def get_campus():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute('select * from CAMPUS')
        lista = [{'id':campus_id,'email':email,'date':date} for (campus_id, email, date) in cursor]
        conn.close()
        return lista
    except:
        return []

# question 1
@app.route('/campus/<question_number>', methods=['GET'])
def get_campus_questions(question_number):
    campus_data = get_campus()
    data = campus_questions.resolve_question(int(question_number)-1, campus_data)
    return json.dumps({'status':'success', 'data': data})

## post del sleep
@app.route('/sleep', methods=['POST'])
def post_sleep():
    content = request.get_json(silent=True)
    mail = content['email']
    date = content['date']
    type = content['type']
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        if type=='start':
            print 'entro'
            cursor.execute('insert into SLEEP values(null, %s, %s, null)', (mail, date))
        else:
            cursor.execute('update SLEEP SET end_date=%s WHERE email = %s AND end_date is NULL',(date,mail))
        conn.commit()
    except:
        conn.rollback()
        return json.dumps({'status':'error'}), 505
    return json.dumps({'status':'succes'}), 200

## get del sleep
def get_sleep():
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        cursor.execute('select * from SLEEP')
        lista = [{'id':campus_id,'email':email,'date':date, 'type': tipo} for (campus_id, email, date, tipo) in cursor]
        conn.close()
        return lista
    except:
        conn.close()
        return []

## post de eventos
@app.route('/event', methods=['POST'])
def post_eventos():
    content = request.get_json(silent=True)
    mail = content['email']
    date = content['date']
    start_date = content['start_date']
    end_date = content['end_date']
    type = content['type']
    recomended = content['recommended']
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        cursor.execute('insert into EVENTOS values(null, %s, %s, %s, %s, %s, %s)', (mail, start_date,end_date,type,recomended,date))
        conn.commit()
    except:
        conn.rollback()
        return json.dumps({'status':'error'}), 505
    return json.dumps({'status':'succes'}), 200

## get de eventos
def get_eventos():
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        cursor.execute('select * from EVENTOS')
        lista = [{'id':campus_id,'email':email,'date':date,'start_date':start_date,'end_date':end_date, 'type': tipo, 'recomended': recomended} for (campus_id, email, start_date,end_date, tipo, recomended, date) in cursor]
        conn.close()
        return lista
    except:
        conn.close()
        return []
@app.route('/events/<question_number>', methods=['GET'])
def get_events_questions(question_number):
    events_data = get_eventos()
    data = events_questions.resolve_question(int(question_number)-1, events_data)
    return json.dumps({'status':'success', 'data': data})
## post de interaccion
@app.route('/interaccion', methods=['POST'])
def post_interaccion():
    content = request.get_json(silent=True)
    mail = content['email']
    date = content['date']
    tipo = content['tipo']
    accion = content['accion']
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        cursor.execute('insert into INTERACCION values(null, %s, %s, %s, %s)', (mail, date,tipo,accion))
        conn.commit()
    except:
        conn.rollback()
        return json.dumps({'status':'error'}), 505
    return json.dumps({'status':'succes'}), 200

## get de interaccion
@app.route('/interaccion',methods=['GET'])
def get_interaccion():
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        cursor.execute('select * from INTERACCION')
        lista = [{'id':interaccion_id,'email':email,'date':date,'tipo':tipo,'accion':accion} for (interaccion_id, email, date,tipo,accion) in cursor]
        conn.close()
        return json.dumps({'status':'succes','elementos':lista}),200
    except:
        conn.close()
        return json.dumps({'status':'error'}), 505

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)