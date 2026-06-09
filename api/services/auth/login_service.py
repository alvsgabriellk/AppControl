from database import db, Usuario
from utils import verificar_senha_hash
from sqlalchemy import select
from flask_jwt_extended import create_access_token

def login_ok(email, senha):
    usuario = db.session.execute(
        select(Usuario).where(
            Usuario.email == email
        )
    ).scalar_one_or_none()

    if not usuario:
        return {"error": "Email ou Senha inválidos"}, 400
    
    if not verificar_senha_hash(usuario.senha, senha):
        return {"error": "Email ou Senha inválidos"}, 400
    
    token = create_access_token(identity=str(usuario.id))

    return {
        "msg": "Usuário logado!",
        "token": token
        }, 200