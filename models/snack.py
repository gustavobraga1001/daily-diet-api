from database import db

class Snack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)  # Removido parênteses desnecessários
    isInside = db.Column(db.Boolean, nullable=False)  # Corrigido o tipo e nome da coluna
