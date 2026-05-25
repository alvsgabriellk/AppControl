from database import db
from datetime import datetime

class Manutencao(db.Model):
    __tablename__ = "manutencoes"

    id = db.Column(db.Integer, primary_key=True)
    veiculo_id = db.Column(db.Integer, db.ForeignKey("veiculos.id"), nullable=False)
    oficina_id = db.Column(db.Integer, db.ForeignKey("oficinas.id"), nullable=False)
    tipo_manutencao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Numeric)
    km_manutencao = db.Column(db.Integer)
    data_manutencao = db.Column(db.DateTime, default=datetime.utcnow)
    garantia_dias = db.Column(db.Integer)