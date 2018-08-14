import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/easy')
def easy():
    return render_template("easy.html")

@app.route('/medium')
def medium():
    return render_template("medium.html")

@app.route('/hard')
def hard():
    return render_template("hard.html")

@app.route('/master')
def master():
    return render_template("master.html")


@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
            