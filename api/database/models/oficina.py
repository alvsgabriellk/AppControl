from database import db
from datetime import datetime

class Oficina(db.Model):
    __tablename__ = "oficinas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    responsavel = db.Column(db.String(100))
    endereco = db.Column(db.String(200))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(50))
    data_cadastro = db.Column(db.DateTime,default=datetime.utcnow)
    
    # RELACIONAMENTO
    manutencoes = db.relationship(
        "Manutencao",
        backref="oficina",
        lazy=True
    )