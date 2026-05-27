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
    Clique no link abaixo para confirmar seu email
    {link}
    Caso você não tenha criado uma conta, ignore este email.
    """

    mail.send(msg)


def enviar_recuperacao(usuario):

    token = gerar_token(usuario.email)

    link = f"http://localhost:5000/auth/resetar-senha/{token}"

    msg = Message(
        subject="Recuperar senha",
        sender=current_app.config["MAIL_USERNAME"],
        recipients=[usuario.email]
    )

    msg.body = f"""
    Olá, {usuario.nome}!
    Clique no link abaixo para resetar sua senha
    {link}
    Caso você não tenha solicitado o envio de recuperação de senha, então desconsidere este email.
    """

    mail.send(msg)