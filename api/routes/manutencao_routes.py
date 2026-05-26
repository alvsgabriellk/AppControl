from flask import request, jsonify
from controllers import (
    manutencao_dados,
    manutencoes_lista,
    manutencoes_remover,
    manutencoes_atualizar,
    manutencoes_buscar
)
from routes import mant_bp

@mant_bp.route("/nova-manutencao", methods=["POST"])
def nova_manutencao():
    dados = request.get_json()

    resposta, status = manutencao_dados(dados)

    return jsonify(resposta), status

@mant_bp.route("/manutencoes", methods=["GET"])
def listar_manutencoes():

    resposta, status = manutencoes_lista()

    return jsonify(resposta), status


@mant_bp.route("/remover", methods=["DELETE"])
def remover_manutencao():
    dados = request.get_json()

    resposta, status = manutencoes_remover(dados)

    return jsonify(resposta), status


@mant_bp.route("/atualizar", methods=["PUT"])
def atualizar_manutencao():
    dados = request.get_json()

    resposta, status = manutencoes_atualizar(dados)

    return jsonify(resposta), status


@mant_bp.route("/buscar", methods=["GET"])
def buscar_manutencao():
    dados = request.get_json()

    resposta, status = manutencoes_buscar(dados)

    return jsonify(resposta), status

