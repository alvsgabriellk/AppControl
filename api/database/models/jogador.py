from database import db

class Jogador(db.Model):
    __tablename__ = "jogadores"

    id_jogador = db.Column(
        db.Integer, primary_key=True,
        autoincrement=True, nullable=False
    )
    nome = db.Column(db.String(100))
    posicao = db.Column(db.String(100))
    id_equipe_fk = db.Column(db.Integer, db.ForeignKey("equipes.id_equipe"))