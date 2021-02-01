from flask import Flask, render_template

#include lists and functions from python file called fake_data
from fake_data import dogs, posts, get_dog_by_handle, get_posts_by_handle

from sec import hi #import function hi() from python file, sec.py

#app object contains templates and variable of static folder name url path
app = Flask(__name__, template_folder="templates", static_url_path = '/static')

#call and use app object
@app.route('/') # location of page => runs function feed()
def feed():
    return render_template('feed.html', posts=posts, get_dog_by_handle = get_dog_by_handle)

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
def dog(handle):
    dog = get_dog_by_handle(handle)
    return render_template('dog.html', dog = dog, posts = get_posts_by_handle(handle) )


"""
@app.route('/base') 
def base():
    return render_template('base.html')
"""


# run following main code in python if it exist
if __name__ == "__main__": 
    app.run(debug=True)
    #app.run(debug=True, port = 3000) # specify what port to use