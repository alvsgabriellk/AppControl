from database import db, Manutencao, Veiculo, Oficina
from sqlalchemy import select

def manutencao_ok(veiculo_id, oficina_id, tipo_manutencao, valor, km_manutencao, garantia_dias):
    veiculo = db.session.execute(
        select(Veiculo).where(
            Veiculo.id == veiculo_id
        )
    ).scalar_one_or_none()

    if not veiculo:
        return {"error": "Veiculo não encontrado"}, 404
    
    oficina = db.session.execute(
        select(Oficina).where(
            Oficina.id == oficina_id
        )
    ).scalar_one_or_none()

    if not oficina:
        return {"error": "Oficina não encontrada"}, 404
    
    if km_manutencao < veiculo.km_atual:
        return {"error": "Km atualmente na manutenção não pode ser menor que o km atual registrado!"}, 400
    
    veiculo.km_atual = km_manutencao
    
    manutencao = Manutencao(
        veiculo_id=veiculo.id,
        oficina_id=oficina.id,
        tipo_manutencao=tipo_manutencao,
        valor=valor,
        km_manutencao=km_manutencao,
        garantia_dias=garantia_dias
    )

    db.session.add(manutencao)
    db.session.commit()

    return {"msg": "Manutenção realizada!"}, 201

def manutencoes_lista_ok():
    manutencoes = db.session.execute(
        select(Manutencao)
    ).scalars().all()

    if not manutencoes:
        return {"error": "Não existe nenhuma manutenção cadastrada!"}, 404

    manutencoes_json = []

    for manutencao in manutencoes:
        manutencoes_json.append({
            "manutencao_id": manutencao.id,
            "veiculo_id": manutencao.veiculo_id,
            "oficina_id": manutencao.oficina_id,
            "tipo_manutencao": manutencao.tipo_manutencao,
            "valor": float(manutencao.valor),
            "km_manutencao": manutencao.km_manutencao,
            "data_manutencao": manutencao.data_manutencao,
            "garantia_dias": manutencao.garantia_dias
        })

    return {"manutencoes": manutencoes_json}, 200


def manutencoes_remover_ok(id):
    manutencao = db.session.get(Manutencao, id)

    if not manutencao:
        return {"error": "Manutenção não encontrada"}, 404

    db.session.delete(manutencao)
    db.session.commit()

    return {"msg": "Manutenção removida!"}, 200


def manutencoes_atualizar_ok(dados):
    id = dados["id"]

    manutencao = db.session.get(Manutencao, id)

    if not manutencao:
        return {"error": "Manutenção não encontrada"}, 404

    if "tipo_manutencao" in dados:
        manutencao.tipo_manutencao = dados["tipo_manutencao"]

    if "valor" in dados:
        manutencao.valor = float(dados["valor"])

    if "garantia_dias" in dados:
        manutencao.garantia_dias = int(dados["garantia_dias"])

    db.session.commit()

    return {"msg": "Manutenção atualizada!"}, 200


def manutencoes_buscar_ok(id):
    manutencao = db.session.get(Manutencao, id)

    if not manutencao:
        return {"error": "Manutenção não encontrada"}, 404

    return {
        "manutencao": {
            "manutencao_id": manutencao.id,
            "veiculo_id": manutencao.veiculo_id,
            "oficina_id": manutencao.oficina_id,
            "tipo_manutencao": manutencao.tipo_manutencao,
            "valor": float(manutencao.valor),
            "km_manutencao": manutencao.km_manutencao,
            "data_manutencao": manutencao.data_manutencao,
            "garantia_dias": manutencao.garantia_dias
        }
    }, 200