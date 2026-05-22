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