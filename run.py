from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import (StringField, BooleanField, DateTimeField, 
                    RadioField, SelectField, TextField,
                    TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] ='mysecretkey'

# 1st- Flask Basics

# @app.route('/')
# def indexpage():
#     name = "Baruch"
#     letters = list(name)
#     pup_dictionary = {'pup_name': 'Sammy'}
#     puppies = ['Spot', 'Dot', 'Wigs']
#     user_logged_in = False
#     return render_template('basic.html', name=name, letters=letters, pup_dictionary=pup_dictionary, puppies=puppies, user_logged_in=user_logged_in)

# @app.route('/information')
# def info():
#     return "<h1>Puppies are cute!</h1>"

# @app.route('/puppy/<name>')
# def puppy(name):
#     return "100th Letter: {}".format(name[100])

# @app.route('/puppy_name/<name>')
# def puppylatin(name):
#     pupname = ''
#     if name[-1] =='y':
#         pupname =name[:-1] + 'iful'
#     else:
#         pupname = name + 'y'
    
#     return f"Hello {name} Your puppy latin name is: {pupname}"

# @app.route('/')
# def index():
#     return render_template('home.html')

# @app.route('/puppy/<name>')
# def pup_name(name):
#     return render_template('puppy.html', name=name)



# Second - Flask Templates


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/signup_form')
# def signup_form():
#     return render_template('signup.html')

# @app.route('/thank_you')
# def thank_you():
#     first = request.args.get('first')
#     last = request.args.get('last')

#     return render_template('thankyou.html', first=first, last=last)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404


# 3rd - Flask Forms

class InfoForm(FlaskForm):

    breed = StringField("What breed are you?", validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField('Please choose your mood:', choices=[('mood_one', 'Happy'),('mood_two','Excited')])
    food_choice = SelectField(u'Pick your favorite food:', choices=[('chi','Chicken'),('bf','Beef'),('fi','Fish')])
    feedback = TextAreaField()
    submit = SubmitField("Submit")
    
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     breed = False
#     form =InfoForm()
#     if form.validate_on_submit():
#         breed = form.breed.data
#         form.breed.data = ''
#     return render_template('index.html', form=form, breed=breed)

@app.route('/', methods=['GET', 'POST'])
def index():
    form =InfoForm()
    if form.validate_on_submit():
        session['breeed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thank_you'))

    return render_template('index.html',form=form)

@app.route('/thank_you')
def thank_you():
    return render_template('thankyou.html')

if __name__=='__main__':
    app.run(debug=True)