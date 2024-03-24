from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Shioso@2023@localhost:5432/flask_course'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# Create all tables defined in the models
db.create_all()

# Route to create a new user
@app.route('/create_user/<username>')
def create_user(username):
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return f'User {username} created successfully.'

if __name__ == '__main__':
    app.run(debug=True)
