from flask import Flask
from flask import render_template

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hellooooooooooooooooo....'

@app.route('/blogs')
def blogs():
    return 'This is a blog.'

@app.route('/blog/2020/dog')
def blog2():
    return 'This is a blog about dog.'

@app.route('/aboutus.html')
def about():
    return render_template('aboutus.html')

@app.route('/index.html')
def index():
    return render_template('index.html')