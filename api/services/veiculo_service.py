from database import db, Veiculo, Usuario
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

def veiculo_ok(usuario_id, placa, renavan, marca, modelo, km_compra, km_atual):
    usuario = db.session.execute(
        select(Usuario).where(
            Usuario.id == usuario_id
        )
    ).scalar_one_or_none()

    if not usuario:
        return {"error": "Usuário não encontrado"}, 404
    
    veiculo = Veiculo(
        usuario_id=usuario.id, placa=placa,
        renavan=renavan, marca=marca, 
        modelo=modelo, km_compra=km_compra,
        km_atual=km_atual
    )

    try:
        db.session.add(veiculo)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

        return {"error": "Veiculo já foi cadastrado"}, 409
    
    return {"msg": "Veiculo cadastrado!"}, 201

def veiculos_lista_ok():
    veiculos = db.session.execute(
        select(Veiculo)
    ).scalars().all()

    if not veiculos:
        return {"error": "Não existe nenhum veiculo cadastrado!"}, 404
    
    veiculos_json = []

    for veiculo in veiculos:
        veiculos_json.append({
            "veiculo_id" : veiculo.id,
            "usuario_id": veiculo.usuario_id,
            "placa": veiculo.placa,
            "renavan": veiculo.renavan,
            "marca": veiculo.marca,
            "modelo": veiculo.modelo,
            "km_compra": veiculo.km_compra,
            "km_atual": veiculo.km_atual,
            "data_cadastrado": veiculo.data_cadastro
        })
    
    return {"veiculos": veiculos_json}, 200

def veiculos_remover_ok(id):
    veiculo = db.session.execute(
        select(Veiculo).where(
            Veiculo.id == id
        )
    ).scalar_one_or_none()

    if not veiculo:
        return {"error": "Veiculo não encontrado"}, 404
    
    db.session.remove(veiculo)
    db.session.commit()

    return {"msg": "Veiculo deletado!"}, 200