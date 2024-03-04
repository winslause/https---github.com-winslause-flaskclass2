from flask import app, app, Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'wenslause300@gmail.com'
app.config['MAIL_PASSWORD'] = 'Shioso@2023'
app.config['MAIL_USER_TLS'] = False
app.config['MAIL_USER_SSL'] = True

mail = Mail(app)


@app.route("/")
def index():
    msg = Message('Hello', sender='wenslause300@gmail.com', recipients=['wenbusale383@gmail.com'])
    msg.body = "Hello wenslause, i tried to send youa message using flask localhost as a learning practice"
    mail.send(msg)
    return 'Message sent successfully'


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(debug=True)
