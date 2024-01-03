from .base import db

class Subscription(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(length=50), nullable=False)
    # Aquí podrías añadir más campos relacionados con la suscripción, si es necesario.

    def __repr__(self):
        return f'Subscription {self.type}'