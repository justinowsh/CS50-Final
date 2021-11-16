from flask import Flask, redirect, render_template, request, flash, session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

@app.route("/")
def index():
    """Show latest file data"""
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user id
    session.clear()
    if request.method == "POST":
        pass
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run()