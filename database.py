from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__, template_folder="templates")
global msg
try:
    with sql.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("CREATE TABLE students(name TEXT, addr MESSAGE_TEXT"
                     ", city TEXT, pin TEXT)")
        cur.execute("INSERT INTO students(name, addr, city, pin)"
                     "VALUES ('wens', 'nairobi', 'Nairobi', '0987')")
        con.commit()
        msg = "Record successfully added"

except:
    con.rollback()
    msg = "Error in insert operation"
finally:
    con.close()


@app.route('/')
def showlist():
    return render_template('home.html')


@app.route('/list')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    return render_template('list.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
