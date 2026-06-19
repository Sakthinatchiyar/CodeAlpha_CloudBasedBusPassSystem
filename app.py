from flask import Flask, render_template, request
import sqlite3
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/submit', methods=['POST'])
def submit():

    name = request.form['name']
    source = request.form['source']
    destination = request.form['destination']

    if source == "Chennai" and destination == "Tambaram":
        price = 20
    else:
        price = 50

    pass_id = str(uuid.uuid4())[:8]

    conn = sqlite3.connect('buspass.db')
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO buspass(name,source,destination,price,passid) VALUES (?,?,?,?,?)",
        (name,source,destination,price,pass_id)
    )

    conn.commit()
    conn.close()

    return render_template(
        'success.html',
        passid=pass_id,
        price=price
    )

if __name__ == '__main__':
    app.run(debug=True)