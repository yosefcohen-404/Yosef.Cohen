from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about')
def hello_about():
    return 'Hello About!'


@app.route('/home')
def hello_home():
    return redirect('/')


@app.route('/customers')
def customer_signup():
    sign = True
    if sign:
        return redirect(url_for('hello_home'))
    else:
        return 'Please signup!'


if __name__ == '__main__':
    app.run()
