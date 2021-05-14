from os import abort
from flask import render_template, url_for, flash, redirect, request
from forum import app, db, bcrypt
from forum.forms import RegistrationForm, LoginForm, QuestionForm, AnswerForm
from forum.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    questionForm = QuestionForm()
    answerForm = AnswerForm()
    if questionForm.validate_on_submit():
        post = Post(title=questionForm.title.data, content=questionForm.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your Post has been created", 'success')
        return redirect(url_for('home'))
    posts = Post.query.all()
    return render_template('home.html', posts=posts, questionForm=questionForm)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please check email and password", 'danger')
    return render_template('login.html', title="Login", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title="Account")


@app.route('/post/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post has been deleted.", 'success')
    return redirect(url_for('home'))
