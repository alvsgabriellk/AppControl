from flask_mail import Message
from flask import current_app, render_template
from utils import mail

from itsdangerous import URLSafeTimedSerializer

def gerar_token(email):

    serializer = URLSafeTimedSerializer(
        current_app.config["KEY_API"]
    )

    token = serializer.dumps(email, salt="email-confirm")

    return token

from itsdangerous import URLSafeTimedSerializer
from flask import current_app


def validar_token(token):

    serializer = URLSafeTimedSerializer(
        current_app.config["KEY_API"]
    )

    try:

        email = serializer.loads(
            token,
            salt="email-confirm",
            max_age=3600
        )

        return email

    except:
        return None