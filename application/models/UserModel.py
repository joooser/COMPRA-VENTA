from .base import db, bcrypt, UserMixin, datetime, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    signup_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    password_hash = db.Column(db.String(length=60), nullable=False)
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'), default=1)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), default=1)
    
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return f'User {self.email}'