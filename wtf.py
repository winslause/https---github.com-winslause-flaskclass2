from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)

app.secret_key = "Flask"


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm
    if request.method == 'POST':
        if form.validate()==False:
            flash('All the required fields must be filled')
            return render_template("contact.html", form=form)
        else:
            return "success"
    elif request.method == 'GET':
        return render_template("contact.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
