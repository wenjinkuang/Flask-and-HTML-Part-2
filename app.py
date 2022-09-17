## importing the flask package 
from flask import Flask, render_template

## creating a Flask App with the name app 
app = Flask(__name__)

## creating and styling homepage using flask render_template homepage and styles2
@app.route('/')
def home():
    return render_template('home.html')

## creating and styling contact page using flask render_template contact and styles3
@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)