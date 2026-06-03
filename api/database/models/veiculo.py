from database import db
from datetime import datetime
class Veiculo(db.Model):
    __tablename__ = "veiculos"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    placa = db.Column(db.String(10),unique=True,nullable=False)
    renavan = db.Column(db.String(20),unique=True,nullable=False)
    marca = db.Column(db.String(50),nullable=False)
    modelo = db.Column(db.String(50),nullable=False)
    marca_modelo = db.Column(db.String(30), nullable=False)
    ano_modelo = db.Column(db.Integer, nullable=False)
    cor = db.Column(db.String(30), nullable=False)
    km_compra = db.Column(db.Float)
    km_atual = db.Column(db.Float)
    data_cadastro = db.Column(db.DateTime,default=datetime.utcnow)

    # RELACIONAMENTO
    manutencoes = db.relationship(
        "Manutencao",
        backref="veiculo",
        lazy=True
    )