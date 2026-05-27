from database import db, Usuario
from utils import gerar_senha_hash
from services.auth.email_service import enviar_confirmacao
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

        return {"error": "Esse email já está sendo usado!"}, 409
    
    enviar_confirmacao(usuario)
    return {"msg": "Usuário cadastrado!"}, 201