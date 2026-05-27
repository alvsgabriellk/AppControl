from flask_mail import Message
from flask import current_app
from utils import gerar_token, mail

def enviar_confirmacao(usuario):

    token = gerar_token(usuario.email)

    link = f"http://localhost:5000/auth/confirmar-email/{token}"

    msg = Message(
        subject="Confirme seu email",
        sender=current_app.config["MAIL_USERNAME"],
        recipients=[usuario.email]
    )

    msg.body = f"""
    Olá, {usuario.nome}!
    Clique no link abaixo para confirmar seu email:
    {link}
    Se você não criou uma conta, ignore o este email;
    """

    mail.send(msg)