from flask import request, jsonify
from database import db, Usuario
from routes import auth_bp
from controllers import register_dados

@auth_bp.route("/sign-up", methods=["POST"])
def cadastro_usuario():
    dados = request.get_json()

    resposta, status = register_dados(dados)

    return jsonify({"msg": resposta}), status
