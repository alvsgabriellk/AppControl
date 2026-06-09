from flask import request, jsonify
from routes import ofic_bp
from controllers import (
    oficina_dados,
    oficinas_lista,
    oficinas_remover,
    oficinas_atualizar,
    oficinas_buscar
)
from flask_jwt_extended import jwt_required

@ofic_bp.route("/nova-oficina", methods=["POST"])
@jwt_required()
def nova_oficina():
    dados = request.get_json()

    resposta, status = oficina_dados(dados)

    return jsonify(resposta), status

@ofic_bp.route("/oficinas", methods=["GET"])
@jwt_required()
def listar_oficinas():

    resposta, status = oficinas_lista()

    return jsonify(resposta), status


@ofic_bp.route("/remover", methods=["DELETE"])
@jwt_required()
def remover_oficina():
    dados = request.get_json()

    resposta, status = oficinas_remover(dados)

    return jsonify(resposta), status


@ofic_bp.route("/atualizar", methods=["PUT"])
@jwt_required()
def atualizar_oficina():
    dados = request.get_json()

    resposta, status = oficinas_atualizar(dados)

    return jsonify(resposta), status


@ofic_bp.route("/buscar", methods=["GET"])
@jwt_required()
def buscar_oficina():
    dados = request.get_json()

    resposta, status = oficinas_buscar(dados)

    return jsonify(resposta), status