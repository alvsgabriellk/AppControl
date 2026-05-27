from routes import auth_bp
from services import enviar_recuperacao
from utils import validar_token, gerar_senha_hash
from database import Usuario, db
from sqlalchemy import select
from flask import request

@auth_bp.route("/confirmar-email/<token>")
def confirmar_email(token):

    email = validar_token(token)

    if not email:
        return {"error": "Token inválido"}

    usuario = db.session.execute(
        select(Usuario).where(
            Usuario.email == email
        )
    ).scalar_one_or_none()

    usuario.verificado = True

    db.session.commit()

    return {"message": "Email confirmado"}