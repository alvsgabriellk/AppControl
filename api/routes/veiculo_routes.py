from flask import request, jsonify
from routes import veic_bp
from controllers import veiculos_dados, veiculos_lista

@veic_bp.route("/novo-veiculo", methods=["POST"])
def novo_veiculo():
    dados = request.get_json()

    resposta, status = veiculos_dados(dados)

    return jsonify(resposta), status

@veic_bp.route("/veiculos", methods=["GET"])
def listar_veiculos():

    resposta, status = veiculos_lista()

    return jsonify(resposta), status
