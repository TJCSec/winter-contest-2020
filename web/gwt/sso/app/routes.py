from flask import jsonify, request, render_template, redirect, url_for, flash, abort
from flask import current_app as app
from flask_login import current_user, login_required, login_user, logout_user

from .models import db, User
from .forms import LoginForm, RegisterForm
from .token import get_token, get_pubkey
from .utils import is_url, is_safe_url, make_url

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('profile'))
  login_form = LoginForm()
  if login_form.validate_on_submit():
    user = login_form.get_user()
    login_user(user)
    flash(f'Logged in as {user.username}', 'success')
    next_redir = request.args.get('next')
    if not is_safe_url(next_redir):
      return abort(400)
    return redirect(next_redir or url_for('profile'))
  return render_template('login.html', login_form=login_form)

@app.route('/logout')
def logout():
  logout_user()
  flash('Logged out', 'success')
  return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('profile'))
  register_form = RegisterForm()
  if register_form.validate_on_submit():
    user = User(username=register_form.username.data, password=register_form.password.data)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    flash(f'Logged in as {user.username}', 'success')
    return redirect(url_for('profile'))
  return render_template('register.html', register_form=register_form)

@app.route('/profile')
@login_required
def profile():
  return render_template('profile.html')

@app.route('/pubkey')
def pubkey():
  return jsonify(get_pubkey())

@app.route('/authorize')
@login_required
def authorize():
  url = request.args.get('next')
  if not is_url(url):
    return abort(400)
  return render_template('authorize.html', url=url, url_token=make_url(url, {'token': get_token()}))
