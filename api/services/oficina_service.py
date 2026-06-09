
from database import db, Oficina
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from flask_jwt_extended import get_jwt_identity

def oficina_ok(nome, telefone, responsavel, endereco, cidade, estado):
    usuario_id = int(get_jwt_identity())
    
    oficina = Oficina(
        usuario_id=usuario_id,
        nome=nome,
        telefone=telefone,
        responsavel=responsavel,
        endereco=endereco,
        cidade=cidade,
        estado=estado
    )

    try:
        db.session.add(oficina)
        db.session.commit()
    
    except IntegrityError:
        db.session.rollback()

        return {"error": "Oficina já foi cadastrada"}, 409
    
    return {"msg": "Oficina cadastrada!"}, 201

def oficinas_lista_ok():
    usuario_id = int(get_jwt_identity())

    oficinas = db.session.execute(
        select(Oficina).where(
            Oficina.usuario_id == usuario_id
        )
    ).scalars().all()

    if not oficinas:
        return {"error": "Não existe nenhuma oficina cadastrada!"}, 404

    oficinas_json = []

    for oficina in oficinas:
        oficinas_json.append({
            "oficina_id": oficina.id,
            "nome": oficina.nome,
            "telefone": oficina.telefone,
            "responsavel": oficina.responsavel,
            "endereco": oficina.endereco,
            "cidade": oficina.cidade,
            "estado": oficina.estado,
            "data_cadastro": oficina.data_cadastro
        })

    return {"oficinas": oficinas_json}, 200


def oficinas_remover_ok(id):
    usuario_id = int(get_jwt_identity())

    oficina = db.session.execute(
        select(Oficina).where(
            Oficina.id == id,
            Oficina.usuario_id == usuario_id
        )
    ).scalar_one_or_none()

    if not oficina:
        return {"error": "Oficina não encontrada"}, 404

    db.session.delete(oficina)
    db.session.commit()

    return {"msg": "Oficina removida!"}, 200


def oficinas_atualizar_ok(dados):
    id = dados["id"]
    usuario_id = int(get_jwt_identity())

    oficina = db.session.execute(
        select(Oficina).where(
            Oficina.id == id,
            Oficina.usuario_id == usuario_id
        )
    ).scalar_one_or_none()

    if not oficina:
        return {"error": "Oficina não encontrada"}, 404

    if "nome" in dados:
        oficina.nome = dados["nome"]

    if "telefone" in dados:
        oficina.telefone = dados["telefone"]

    if "responsavel" in dados:
        oficina.responsavel = dados["responsavel"]

    if "estado" in dados:
        oficina.estado = dados["estado"]
    
    if "cidade" in dados:
        oficina.cidade = dados["cidade"]

    if "endereco" in dados:
        oficina.estado = dados["endereco"]

    db.session.commit()

    return {"msg": "Oficina atualizada!"}, 200


def oficinas_buscar_ok(dados):
    
    usuario_id = int(get_jwt_identity())

    if "id" in dados:
        oficina = db.session.execute(
            select(Oficina).where(
                Oficina.id == dados["id"],
                Oficina.usuario_id == usuario_id
            )
        ).scalar_one_or_none()

    elif "nome" in dados:
        oficina = db.session.execute(
            select(Oficina).where(
                Oficina.nome == dados["nome"],
                Oficina.usuario_id == usuario_id
            )
        ).scalar_one_or_none()

    else:
        return {"error": "Informe id ou nome"}, 400

    if not oficina:
        return {"error": "Oficina não encontrada"}, 404

    return {
        "oficina": {
            "oficina_id": oficina.id,
            "nome": oficina.nome,
            "telefone": oficina.telefone,
            "responsavel": oficina.responsavel,
            "endereco": oficina.endereco,
            "cidade": oficina.cidade,
            "estado": oficina.estado,
            "data_cadastro": oficina.data_cadastro
        }
    }, 200
