# For using Flask
from flask import Flask

# For rendering templates
from flask import render_template

# For Flask-Bootstrap
from flask_bootstrap import Bootstrap

# For wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# For session, redirect
from flask import session, redirect, url_for

app = Flask(__name__)
# the secret key will be stored in an environment variable later
# keeping it simple for learning purposes
app.config['SECRET_KEY'] = 'flasky_app_june_2022'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    # return '<h1>Hello World!</h1>'
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    # return '<h1>Hello {}!<h1>'.format(name)
    return render_template('user.html', name=name)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')