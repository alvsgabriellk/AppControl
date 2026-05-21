from database import db, Usuario
from utils import gerar_senha_hash
from sqlalchemy.exc import IntegrityError

def register_ok(nome, email, senha):
    senha_hash = gerar_senha_hash(senha)
    
    usuario = Usuario(
        nome=nome,
        email=email,
        senha=senha_hash
    )

    try:
        db.session.add(usuario)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

        return {"error": "Email já está sendo usado!"}, 409
    
    return {"msg": "Usuário cadastrado!"}, 201