from app import app

from flask import render_template

@app.route('/')
@app.route('/index')
def home():
    school_count = 350
    return render_template('home.html', count = school_count)
