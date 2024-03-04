from flask import render_template_string, make_response, Flask,redirect, request, url_for, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__, template_folder='templates')

@app.route('/upload')
def upload_file():
    return render_template("upload.html")

@app.route('/uploader', methods=["POST", "GET"])
def uploaded_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "file uploaded successfully"
        
        
            

if __name__ == '__main__':
    app.run(debug=True)