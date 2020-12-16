from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import EqualTo, InputRequired
from sqlalchemy import func

from .models import User
from .utils import VALID_USERNAME

class LoginForm(FlaskForm):
  username = StringField("Username", validators=[InputRequired("Enter your username")])
  password = PasswordField("Password", validators=[InputRequired("Enter your password")])
  submit = SubmitField("Login")

  def get_user(self):
    query = User.query.filter(func.lower(User.username) == self.username.data.lower())
    return query.first()

  def validate_username(self, field):
    if self.get_user() is None:
      raise ValidationError("User does not exist")

  def validate_password(self, field):
    user = self.get_user()
    if not user:
      return
    if not user.check_password(field.data):
      raise ValidationError("Incorrect password")

class RegisterForm(FlaskForm):
  username = StringField("Username", validators=[InputRequired("Enter a username")])
  password = PasswordField("Password", validators=[InputRequired("Enter a password")])
  confirm_password = PasswordField("Confirm Password", validators=[InputRequired("Confirm your password"), EqualTo("password", "Passwords do not match")])
  submit = SubmitField("Register")

  def validate_username(self, field):
    if not VALID_USERNAME.match(field.data):
      raise ValidationError("Username must be contain letters, numbers, or _, and not start with a number")
    if User.query.filter(func.lower(User.username) == field.data.lower()).count():
      raise ValidationError("Username is taken")
