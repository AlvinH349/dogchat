from flask import Flask, render_template, abort #abort- log out

#include lists and functions from python file called fake_data
from fake_data import dogs, posts, get_dog_by_handle, get_posts_by_handle

from sec import hi #import function hi() from python file, sec.py

# https://flask-httpauth.readthedocs.io/en/latest/
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

#app object contains templates and variable of static folder name url path
app = Flask(__name__, template_folder="templates", static_url_path = '/static')

# object that refereances authentication
auth = HTTPBasicAuth()

#set of users for authenthication
users = {
    #"username" :  generate_password_hash("password")
    "Mary": generate_password_hash("Mary")
}

#check password and username through dictionary of pass and users
#if exist, then return username
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

#call and use app object
@app.route('/') # location of page => runs function feed()
@auth.login_required #allow access if pass authnithication 
def feed():
    return render_template('feed.html', posts=posts, get_dog_by_handle = get_dog_by_handle, user=auth.current_user() )

'''
@app.route('/dog') 
def dog():
    posts = {
        "post1", 
        "post2", 
        "post3"
    }
    return render_template('dog.html', dog_name = "Melba", dog_handle = "@melba",
     posts= posts, get_dog_by_handle = get_dog_by_handle)
'''
#add specific user page
@app.route('/dog/<string:handle>') 
@auth.login_required #allow access if pass authnithication 
def dog(handle):
    dog = get_dog_by_handle(handle)
    return render_template('dog.html', dog = dog, posts = get_posts_by_handle(handle) )


"""
@app.route('/base') 
def base():
    return render_template('base.html')
"""

#if users logs out of page as user
@app.route('/logout')
def logout():
    return abort(401)
# 401 - unauthorized
#404 - page not found


# run following main code in python if it exist
if __name__ == "__main__": 
    app.run(debug=True)
    #app.run(debug=True, port = 3000) # specify what port to use