import os
from flask import Flask, render_template  # Importing flask class
"""
creating instance of Flask and storing it in app variable
Flask parameter is the name of the applications
module/package, __name__ is a built in python
varabile, flask needs it to find templates/static files
"""
app = Flask(__name__)


@app.route("/")  # decorator - a way of wrapping functions
# When we browse to root directory ("/") then flask will trigger index function
def index():  # called a view
    return render_template("index.html")


@app.route("/about")
def about():  # called a view
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        # host on IP if can be found if not default to 0.0.0.0
        host=os.environ.get("IP", "0.0.0.0"),
        # post to port if found is not use gateway 5000 commonly used for Flask
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
"""
never have debug = true in a production application or on submission
as it allows arbritary code to run, change to false before submission
"""
