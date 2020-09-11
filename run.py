import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env
"""
creating instance of Flask and storing it in app variable
Flask parameter is the name of the applications
module/package, __name__ is a built in python
varabile, flask needs it to find templates/static files
"""
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")  # decorator - a way of wrapping functions
# When we browse to root directory ("/") then flask will trigger index function
def index():  # called a view
    return render_template("index.html")


@app.route("/about")
def about():  # called a view
    data = []
    with open("data/company.json", "r") as json_data:
        # r means read only and assigning the contents to json_data variable
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


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
