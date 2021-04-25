from flask import Flask, render_template, url_for, request
from data import db_session

app = Flask(__name__)



@app.route('/')
def showSignUp():
    return render_template('first.html')

@app.route('/main')
def showSignUpi():
    return render_template('index.html')

@app.route('/register')
def news():
    return render_template('regist.html')

@app.route('/characters')
def characters():
    return render_template('Hero.html')

@app.route('/login')
def Login():
    return render_template('login.html')


@app.route('/news')
def News():
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)
