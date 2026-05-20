from database import db
from datetime import date

class Partidas(db.Model):
    __tablename__ = "partidas"

    id_partidas = db.Column(
        db.Integer, primary_key=True,
        autoincrement=True, nullable=False
    )
    data = db.Column(db.Date,default=date.today, nullable=False)
    id_time_casa_fk = db.Column(db.Integer, db.ForeignKey("equipe.id_quipe"))
    id_time_visitante_fk = db.Column(db.Integer, db.ForeignKey("equipe.id_equipe"))
    placar_casa = db.Column(db.Integer, nullable=False),
    placar_visitante = db.Column(db.Integer, nullable=False)