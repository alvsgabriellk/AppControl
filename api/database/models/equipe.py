from database import db

class Equipe(db.Model):
    __tablename__ = "equipes"

    id_equipe = db.Column(
        db.Integer, primary_key=True, 
        autoincrement=True, nullable=False
    )
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(50))

    # pelo jogador da pra acessar a equipe ex: jogador.equipe.nome
    jogadores = db.relationship(
        "Jogador",
        backref="equipe",
        lazy=True
    )