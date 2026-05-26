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

