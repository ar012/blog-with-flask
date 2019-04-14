from app import app
from flask import Flask, render_template, redirect, url_for, flash

from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def home():
    user = {'username': 'Rashed'}

    posts = [
        {
            'author': 'Jhon',
            'body': 'This is a beautiful day'
        },
        {
            'author': 'Bob',
            'body': "I'm good today"
        },
        {
            'author': 'Alice',
            'body': 'Got a new job today'
        },
    ]
    return render_template('home.html', title='selftics', user=user, posts=posts)


@app.route('/product')
def product():
    return render_template('product.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
      flash('Login requested for the user {}'.format(form.username.data))
      
      return redirect(url_for('home'))

    return render_template('login.html', title='Sign In Here', form=form)
