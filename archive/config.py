#class Config:
#    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
#    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
#    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
#    SESSION_COOKIE_SECURE = True
#    SESSION_COOKIE_HTTPONLY = True
#    SESSION_COOKIE_SAMESITE = 'Lax'
#
#class DevelopmentConfig(Config):
#    DEBUG = True
#    SESSION_COOKIE_SECURE = False  # Typically, you might not have HTTPS in development
#
#class ProductionConfig(Config):
#    DEBUG = False
#    # Additional production-specific settings
#
#app.config.from_object('application.config.DevelopmentConfig')  # Or 'application.config.ProductionConfig'
