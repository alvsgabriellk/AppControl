from flask import request, jsonify
from routes import ofic_bp
from controllers import oficina_dados

@ofic_bp.route("/nova-oficina", methods=["POST"])
def nova_oficina():
    dados = request.get_json()

    resposta, status = oficina_dados(dados)

    return jsonify(resposta), status