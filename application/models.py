from .extensions import db, login_manager, bcrypt
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=20), nullable=False, unique=True)
    users = db.relationship('User', backref='role', lazy=True)

    def __repr__(self):
        return f'Role {self.name}'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    signup_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(length=30), nullable=False)
    lastname = db.Column(db.String(length=30), nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'))
    
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return f'User {self.username}'

class Subscription(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(length=50), nullable=False)
    # Aquí podrías añadir más campos relacionados con la suscripción, si es necesario.

    def __repr__(self):
        return f'Subscription {self.type}'

class Vehicle(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    brand = db.Column(db.String(length=30), nullable=False)
    model = db.Column(db.String(length=30), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    color = db.Column(db.String(length=30), nullable=False)
    type = db.Column(db.String(length=30), nullable=False)
    usage = db.Column(db.String(length=30), nullable=False)
    plate = db.Column(db.String(length=15), nullable=False)
    serial_motor = db.Column(db.String(length=30), nullable=False)
    serial_bodywork = db.Column(db.String(length=30), nullable=False)
    # ...

class Contractor(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    lastname = db.Column(db.String(length=30), nullable=False)
    per_doc_id = db.Column(db.String(length=30), nullable=False)
    birth = db.Column(db.DateTime(), nullable=False)
    civil_status = db.Column(db.String(length=15), nullable=False)
    residence = db.Column(db.String(length=100), nullable=False)
    # ...

class PropertyTitle(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    n_title = db.Column(db.String(length=30), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    form = db.Column(db.String(length=30), nullable=False)
    # ...

class PropertyDocument(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    notary = db.Column(db.String(length=30), nullable=False)
    n_auth = db.Column(db.Integer(), nullable=False)
    tome = db.Column(db.String(length=30), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    # ...

class Document(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    contractor_seller_id = db.Column(db.Integer(), db.ForeignKey('contractor.id'), nullable=False)
    contractor_buyer_id = db.Column(db.Integer(), db.ForeignKey('contractor.id'), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    type_payment = db.Column(db.String(length=30), nullable=False)
    # Aquí puedes añadir relaciones con ForeignKey si es necesario
    # ...

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'seller', 'buyer', 'car', etc.

    def __repr__(self):
        return f'<Question {self.text}>'

class DocumentTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template_text = db.Column(db.Text, nullable=False)  # Stores the template text

    def __repr__(self):
        return f'<DocumentTemplate {self.id}>'

# No olvides inicializar tu base de datos con db.create_all() después de definir tus modelos,
# especialmente si no estás utilizando Flask-Migrate.