from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("cv.html")


@app.route('/Full cv')
def full_cv():
    return render_template("Full cv page.html")


@app.route('/Contact List')
def cl():
    return render_template("Contact list page.html")


@app.route('/Projects')
def proj():
    return render_template("Projects page.html")


@app.route('/Contact me')
def cm():
    return render_template("Contact me page.html")


@app.route('/assignment8')
def a8():
    return render_template("assignment8.html", name="", hobbies=["Sports", "Reading", "Doing this assignment"])


@app.route('/assignment8b')
def a8ext():
    return render_template("blockA8.html", name="", hobbies=["Sports", "Reading", "Doing this assignment"])


if __name__ == '__main__':
    app.run()
