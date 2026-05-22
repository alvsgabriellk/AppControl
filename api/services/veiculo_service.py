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