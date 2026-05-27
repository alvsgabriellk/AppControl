from routes import auth_bp
from utils import validar_token
from database import Usuario, db
from sqlalchemy import select

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