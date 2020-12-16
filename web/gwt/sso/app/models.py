from . import db, login_manager
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash

login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(32), unique=True)
  _password = db.Column(db.String(96))

  def check_password(self, password):
    return check_password_hash(self.password, password)

  @hybrid_property
  def password(self):
    return self._password

  @password.setter
  def password(self, password):
    self._password = generate_password_hash(password)

  @staticmethod
  @login_manager.user_loader
  def get_by_id(id):
    query = User.query.filter_by(uid=id)
    return query.first()

  @property
  def is_authenticated(self):
    return True

  @property
  def is_active(self):
    return True

  @property
  def is_anonymous(self):
    return False

  def get_id(self):
    return str(self.uid)
