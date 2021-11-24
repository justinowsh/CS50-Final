from flask import redirect, render_template, request, flash, session, url_for
from application.models import User, Entry
from application import app, db, bcrypt
from datetime import datetime, date

@app.route("/")
def index():
    """Show latest file data"""
    return render_template("index.html.j2")

@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Query database for username
        user = User.query.filter_by(username=username).first()
        if not user:
            flash("No such username exists.", "error")
            return render_template("login.html.j2")
        # Ensure username exists and password is correct
        if user and bcrypt.check_password_hash(user.hash, password):
            # Remember which user has logged in
            session["user_id"] = user.id
            flash(f"You are now logged in as {username}.")
            return redirect("/")
        else:
            flash("Incorrect username and/or password.", "error")
            return render_template("login.html.j2")
    else:
        return render_template("login.html.j2")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # Check if username has been taken
        exist_user = User.query.filter_by(username=username).first()
        if exist_user:
            flash(f"The username {username} is taken, please choose a different username.", "error")
            return render_template("register.html.j2")
        # Check if password and confirmation are the same
        if password != confirmation:
            flash(f"Password and confirmation password do not match.", "error")
            return render_template("register.html.j2")
        # Generate a hash for user's password and store it in the users table
        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
        user = User(username=username, hash=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Registered!")
        return render_template("login.html.j2")

    else:
        return render_template("register.html.j2")

@app.route("/newentry", methods=["GET", "POST"])
def newpage():
    if request.method == "POST":
        cheque = request.form.get("cheque")
        cash = request.form.get("cash")
        calc_total = request.form.get("calc_total")
        expected_total = request.form.get("expected_total")
        variance = request.form.get("variance")
        print(f"cheque: {cheque}")
        print(f"cash: {cash}")
        print(f"calc_total: {calc_total}")
        print(f"expected_total: {expected_total}")
        print(f"variance: {variance}")
        
        # Check if user session is not timed out.
        if not session["user_id"]:
            flash("Session timed out, please log in again.", "info")
            return render_template("login.html.j2")
        
        # INSERT values into entry database.
        entry = Entry(user_id=session["user_id"], cheque=cheque, cash=cash, calculated_total=calc_total, expected_total=expected_total, variance=variance)
        db.session.add(entry)
        db.session.commit()
        flash("Entry saved!", "info")
        return render_template("index.html.j2")
    else:
        today = date.today()
        ftoday = today.strftime("%d/%m/%Y")
        return render_template("newentry.html.j2", date=ftoday)

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
    # Query all entries based on current user's session id
    entries = Entry.query.filter_by(user_id=session["user_id"]).all()

    return render_template("history.html.j2", entries=entries)