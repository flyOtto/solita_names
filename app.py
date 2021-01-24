#This file has some issues, so I'm unable to run it. 
import os
from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)

@app.route('/fetch_names', methods=("GET"))
def html_table():

    return render_template('index.html', tables=[dataFrame.to_html(classes='data', header="true")]


if __name__ == '__main__':
    app.run(debug=True)