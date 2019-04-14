from flask import Flask, render_template

app = Flask(__name__)


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


# app.run()
# app.run(port=5000)
app.run(port=5000, debug=True)
