from database import db

class Snack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)  # Alterado para aceitar data e hora
    isInside = db.Column(db.Boolean, nullable=False)  # Nome e tipo ajustados

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "datetime": self.datetime,
            "isInside": self.isInside
        }
