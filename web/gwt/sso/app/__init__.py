from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()
login_manager = LoginManager()

import secrets

def init_ginkoid():
  from .models import User
  password = secrets.token_hex(64)
  ginkoid = User(username='ginkoid', password=password)
  db.session.add(ginkoid)
  db.session.commit()

def create_app():
  app = Flask(__name__, instance_relative_config=False)
  app.config.from_object('config.Config')
  db.init_app(app)
  login_manager.init_app(app)

  with app.app_context():
    from . import routes
    db.create_all()
    try:
      init_ginkoid()
    except IntegrityError:
      pass
    return app
