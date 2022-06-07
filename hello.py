# For using Flask
from flask import Flask

# For rendering templates
from flask import render_template

# For Flask-Bootstrap
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    # return '<h1>Hello World!</h1>'
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    # return '<h1>Hello {}!<h1>'.format(name)
    return render_template('user.html', name=name)