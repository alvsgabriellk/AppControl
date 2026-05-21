from flask import request, jsonify
from routes import veic_bp
from controllers import veiculo_controller 

@veic_bp.route("/novo-veiculo", methods=["POST"])
def novo_veiculo():
    dados = request.get_json()

    resposta, status = veiculo_controller(dados)

    return jsonify(resposta), status
