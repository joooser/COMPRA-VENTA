from flask import Flask
from .extensions import db, bcrypt, login_manager, migrate
from application.logs.logging_config import setup_logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'secret'
#app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)
setup_logging()

# Import routes here
from application import routes