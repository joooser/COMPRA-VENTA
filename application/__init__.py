from flask import Flask
from .extensions.extensions import db, bcrypt, login_manager, migrate
from application.logs.logging_config import setup_logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'secret'
#app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
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


# Import blueprints
from application.routes.routes import main_blueprint
from application.auth.auth_routes import auth_blueprint

# Register blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint, url_prefix='/auth')