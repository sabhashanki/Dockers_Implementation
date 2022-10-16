import pandas as pd
from flask import Flask, request, render_template

df = pd.DataFrame([1,2,3,3,5], columns={'numbers'})

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)