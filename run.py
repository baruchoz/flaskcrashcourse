import re
from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def indexpage():
#     name = "Baruch"
#     letters = list(name)
#     pup_dictionary = {'pup_name': 'Sammy'}
#     puppies = ['Spot', 'Dot', 'Wigs']
#     user_logged_in = False
#     return render_template('basic.html', name=name, letters=letters, pup_dictionary=pup_dictionary, puppies=puppies, user_logged_in=user_logged_in)

@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"

# @app.route('/puppy/<name>')
# def puppy(name):
#     return "100th Letter: {}".format(name[100])

@app.route('/puppy_name/<name>')
def puppylatin(name):
    pupname = ''
    if name[-1] =='y':
        pupname =name[:-1] + 'iful'
    else:
        pupname = name + 'y'
    
    return f"Hello {name} Your puppy latin name is: {pupname}"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html', name=name)


if __name__=='__main__':
    app.run(debug=True)