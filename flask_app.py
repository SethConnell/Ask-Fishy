from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
app = Flask(__name__)
from DBFunctions import *
from SearchAlgorithm import *

@app.route("/", methods=["GET", "POST"])
def question():
    if request.method == 'POST':
            question=request.form['question']
            searchresult = search(question)
            return str(searchresult)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
