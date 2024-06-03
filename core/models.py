from core import db
from datetime import datetime



class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    senha = db.Column(db.String, nullable=False)
    fotos = db.relationship('Foto', backref="usuario",lazy=True)
    
class Fotos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imagem = db.Column(db.String, default="default.png")
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = db.Column(db.Integer,  db.ForeignKey('usuario.id'), nullable=False,)         