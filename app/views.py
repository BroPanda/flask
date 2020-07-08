from flask import render_template, request,redirect
from app import app


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/search/')
def search_page():
    result = request.args['search']
    return render_template('search.html', search=result)
