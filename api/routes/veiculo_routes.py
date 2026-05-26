from flask import request, jsonify
from routes import veic_bp
from controllers import veiculos_dados, veiculos_lista, veiculos_remover

@veic_bp.route("/novo-veiculo", methods=["POST"])
def novo_veiculo():
    dados = request.get_json()

    resposta, status = veiculos_dados(dados)

    return jsonify(resposta), status

@veic_bp.route("/veiculos", methods=["GET"])
def listar_veiculos():

    resposta, status = veiculos_lista()

    return jsonify(resposta), status


@veic_bp.route("/remover", methods=["POST"])
def remover_veiculo():
    dados = request.get_json()

    resposta, status = veiculos_remover(dados)

    return jsonify(resposta), status