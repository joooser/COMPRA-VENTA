from flask import Flask

# Extensions
from .extensions.extensions import db, bcrypt, login_manager, migrate

# Routes
from .routes.routes import main_blueprint
from .routes.auth_routes import auth_blueprint


def init_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

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


    # Blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app