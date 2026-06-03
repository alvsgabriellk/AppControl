from flask import request, jsonify
from routes import veic_bp
from controllers import (
    veiculos_dados, 
    veiculos_lista, 
    veiculos_remover, 
    veiculos_atualizar, 
    veiculos_buscar
)

@veic_bp.route("/novo-veiculo", methods=["POST"])
def novo_veiculo():
    dados = request.get_json()

    resposta, status = veiculos_dados(dados)

    return jsonify(resposta), status

@veic_bp.route("/veiculos", methods=["GET"])
def listar_veiculos():

    resposta, status = veiculos_lista()

    return jsonify(resposta), status


@veic_bp.route("/remover", methods=["DELETE"])
def remover_veiculo():
    dados = request.get_json()

    resposta, status = veiculos_remover(dados)

    return jsonify(resposta), status

@veic_bp.route("/atualizar", methods=["PUT"])
def atualizar_veiculo():
    dados = request.get_json()

    resposta, status = veiculos_atualizar(dados)

    return jsonify(resposta), status

@veic_bp.route("/buscar", methods=["GET"])
def buscar_veiculo():
    dados = request.get_json()

    resposta, status = veiculos_buscar(dados)

    return jsonify(resposta), status