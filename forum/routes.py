from flask import render_template, url_for, flash, redirect, request
from forum import app, db, bcrypt
from forum.forms import RegistrationForm, LoginForm, QuestionForm, AnswerForm
from forum.models import User, Post, Answer
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/about')
def about():
    return render_template('about.html', title="About Us")


@app.route('/account<int:user_id>')
@login_required
def account(user_id):
    users_name = User.query.get(user_id).username
    posts = Post.query.all()
    posts.reverse()
    return render_template('account.html', title=users_name + "'s account", posts=posts)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    qform = QuestionForm()
    aform = AnswerForm()
    if qform.validate_on_submit():
        db.session.add(Post(title=qform.title.data, content=qform.content.data, author=current_user))
        db.session.commit()
        flash("Your Post has been created", 'success')
        return redirect(url_for('home'))
    posts = Post.query.all()
    posts.reverse()
    return render_template('home.html', posts=posts, questionForm=qform, answerForm=aform)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please check email and password", 'danger')
    return render_template('login.html', title="Login", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.session.add(User(username=form.username.data, email=form.email.data, password=hashed_password))
        db.session.commit()
        flash("Your account has been created! You are now able to log in", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)


@app.route('/search', methods=['POST'])
def search():
    searched = request.form['searched']
    posts = Post.query.filter(Post.title.contains(searched)).all()
    posts.reverse()
    return render_template('search.html', posts=posts, searched=searched)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/delete_user/<int:user_id>')
@login_required
def delete_user(user_id):
    if current_user.id == user_id:
        logout_user()
        db.session.delete(User.query.get(user_id))
        db.session.commit()
        flash("Your account has been deleted.", 'success')
        return redirect(url_for('home'))
    return redirect(url_for('home'))


@app.route('/comment/<int:post_id>/', methods=['GET', 'POST'])
@login_required
def comment(post_id):
    form = AnswerForm()
    if form.validate_on_submit():
        db.session.add(Answer(content=form.content.data, post=Post.query.get(post_id), author=current_user))
        db.session.commit()
        flash("Your Answer has been added", 'success')
        return redirect(url_for('home'))
    return redirect(url_for('home'))


@app.route('/delete_post/<int:post_id>')
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if current_user.id == post.user_id:
        db.session.delete(post)
        db.session.commit()
        flash("Post has been deleted.", 'success')
        return redirect(url_for('home'))
    return redirect(url_for('home'))


@app.route('/delete_answer/<int:answer_id>')
@login_required
def delete_answer(answer_id):
    answer = Answer.query.get(answer_id)
    if current_user.id == answer.user_id:
        db.session.delete(answer)
        db.session.commit()
        flash("Answer has been deleted.", 'success')
        return redirect(url_for('home'))
    return redirect(url_for('home'))