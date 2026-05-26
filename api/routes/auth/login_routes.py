from flask import request, jsonify
from routes import auth_bp
from controllers import login_dados

@auth_bp.route("/sign-in", methods=["POST"])
def login():
    dados = request.get_json()

    resposta, status = login_dados(dados)

    return jsonify(resposta), status