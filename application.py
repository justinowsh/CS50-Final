from flask import Flask, redirect, render_template, request, flash, session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

@app.route("/")
def index():
    """Show latest file data"""
    return render_template("index.html.j2")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass
    else:
        return render_template("login.html.j2")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        pass
    else:
        return render_template("register.html.j2")

@app.route("/newpage", methods=["GET", "POST"])
def newpage():
    if request.method == "POST":
        pass
    else:
        return render_template("newpage.html.j2")

@app.route("/logout")
def logout():
    """Logs user out"""
    # clear session
    return render_template("logout.html.j2")


if __name__ == "__main__":
    app.run(debug=True)