from flask_sqlalchemy import SQLAlchemy
from flask import *

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = 'sqlite'

app.app_context().push()

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(78))
    pin = db.Column(db.String(50))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


@app.route('/')
def show_all():
    return render_template("show_all.html", students=Student.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['pin']:
            flash('Please fill all the details', 'error')
        else:
            student = Student(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
            db.session.add(student)
            db.session.commit()
            flash("Data inserted successfully", "success")
            return redirect(url_for('show_all'))

    return render_template('new.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
