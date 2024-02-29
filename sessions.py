from flask import cli, make_response, Flask,redirect, request, url_for, render_template, session


app = Flask(__name__)

app.secret_key='wenslause'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
        "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href='/login'></b>" \
"Click here to login</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method=='POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
<form action="" method="post">
<p><input type="text" name="username"></p>
<p><input type="submit" value="Login"></p>
</form>
'''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index')) 

if __name__ == '__main__':
    app.run(debug=True)