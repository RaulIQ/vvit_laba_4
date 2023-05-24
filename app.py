import requests
from flask import Flask, render_template, request
import psycopg2

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="password",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()
app = Flask(__name__)

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not(username and password):
        return 'Login or password not entered'
    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())
    print(records)
    if not records:
        return 'Data is missing in the database'
    return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
