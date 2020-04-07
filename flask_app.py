from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def question():
    if request.method == 'POST':
            question=request.form['question']
            return "Wow"
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
