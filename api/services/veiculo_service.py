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
    veiculo = db.session.get(Veiculo, id)

    if not veiculo:
        return {"error": "Veiculo não encontrado"}, 404
    
    db.session.delete(veiculo)
    db.session.commit()

    return {"msg": "Veiculo deletado!"}, 200

def veiculos_atualizar_ok(dados):
    id = dados["id"]
    veiculo = db.session.get(Veiculo, id)

    if not veiculo:
        return {"error": "Veiculo não encontrado"}, 404
    
    if "placa" in dados:
        veiculo.placa = dados["placa"]
    
    if "km_atual" in dados:
        if veiculo.km_atual > dados["km_atual"]:
            return {"error": "Digite o km atual válido!"}, 400
        veiculo.km_atual = dados["km_atual"]
    
    db.session.commit()

    return {"msg": "Veiculo atualizado!"}, 200

def veiculos_buscar_ok(dados):

    if "id" in dados:
        veiculo = db.session.get(Veiculo, dados["id"])
    
    elif "placa" in dados:
        veiculo = db.session.execute(
            select(Veiculo).where(
                Veiculo.placa == dados["placa"]
            )
        ).scalar_one_or_none()
        
    elif "renavan" in dados:
        veiculo = db.session.execute(
            select(Veiculo).where(
                Veiculo.renavan == dados["renavan"]
            )
        ).scalar_one_or_none()
    
    else:
        return {"error": "Informe id, placa ou renavan"}, 400
    
    if not veiculo:
        return {"error": "Veiculo não encontrado"}, 404

        
    return {
        "veiculo": {
            "veiculo_id": veiculo.id,
            "usuario_id": veiculo.usuario_id,
            "placa": veiculo.placa,
            "renavan": veiculo.renavan,
            "marca": veiculo.marca,
            "modelo": veiculo.modelo,
            "km_compra": veiculo.km_compra,
            "km_atual": veiculo.km_atual,
            "data_cadastrado": veiculo.data_cadastro
        }
    }, 200
