from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.models import User
from flask_login import login_user, logout_user, current_user
from datetime import timedelta
from .. import db

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates/auth')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('EmailId')
        password = request.form.get('Password')

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash("Please check your credentials !", category='error')
            return redirect(url_for("auth_bp.login"))

        login_user(user, duration=timedelta(seconds=1))
        return redirect(url_for("dashboard_bp.dashboard"))

    return render_template("login.html")


@auth_bp.route('/signup')
def signup():
    return render_template("register.html")


@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('EmailId')
    fname = request.form.get('FirstName')
    lname = request.form.get('LastName')
    password = request.form.get('Password')
    repeat_password = request.form.get('RepeatPassword')

    if password != repeat_password:
        flash("Password did not match !", category='error')
        return redirect(url_for('auth_bp.signup'))

    user = User.query.filter_by(email=email).first()
    # if this returns a user, then the email already exists in database

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash("User already exist !", category='error')
        return redirect(url_for('auth_bp.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, firstname=fname,
                    lastname=lname, password=generate_password_hash(password, method='sha256'))
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    flash("User created successfully, Please login", category='success')
    return redirect(url_for('auth_bp.login'))


@auth_bp.route('/forgot_password')
def forgot_password():
    return render_template("forgot-password.html")


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))