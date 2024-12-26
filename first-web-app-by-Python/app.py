from flask import Flask 

app  = Flask(__name__)

@app.route('/')
@app.route('/about')

def about():
    return "Hey there , I'm a autodidact programmer who is learning to code in Python and Flask and JS is my heart"

def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)