from flask import Flask, redirect, render_template, request, flash, session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "651eca7d0c784040681b160cce51654b1f8998c23d780882be93eb40c5462a1d"
app.permanent_session_lifetime = timedelta(minutes=5)
@app.route("/")
def index():
    """Show latest file data"""
    return render_template("index.html.j2")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        session["user"] = user
        flash(f"You are now logged in as {user}")
        return redirect("/")
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
    session.clear()
    flash("You have been logged out!", "info")
    return redirect("/")

@app.route("/history")
def history():
    """Displays user's history"""
    return render_template("history.html.j2")

if __name__ == "__main__":
    app.run(debug=True)