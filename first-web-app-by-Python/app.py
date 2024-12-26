from flask import Flask 
from flask import render_template
app  = Flask(__name__)

@app.route('/')
@app.route('/about')


def home():
    return render_template('index.html')

def about():
    return render_template('about.html')
 
if __name__ == '__main__':
    app.run(debug=True)