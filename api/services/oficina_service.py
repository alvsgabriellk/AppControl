
from database import db, Oficina
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

def oficina_ok(nome, telefone, responsavel, endereco, cidade, estado):
    oficina = Oficina(
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
    oficinas = db.session.execute(
        select(Oficina)
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
    oficina = db.session.get(Oficina, id)

    if not oficina:
        return {"error": "Oficina não encontrada"}, 404

    db.session.delete(oficina)
    db.session.commit()

    return {"msg": "Oficina removida!"}, 200


def oficinas_atualizar_ok(dados):
    id = dados["id"]

    oficina = db.session.get(Oficina, id)

    if not oficina:
        return {"error": "Oficina não encontrada"}, 404

    if "nome" in dados:
        oficina.nome = dados["nome"]

    if "telefone" in dados:
        oficina.telefone = dados["telefone"]

    if "responsavel" in dados:
        oficina.responsavel = dados["responsavel"]

    if "estado" in dados:
        if "cidade" not in dados:
            return {
                "error": "Ao atualizar o estado, envie a cidade também!"
            }, 400

        oficina.estado = dados["estado"]
        oficina.cidade = dados["cidade"]

    try:
        db.session.commit()

    except IntegrityError:
        db.session.rollback()

        return {"error": "Já existe uma oficina com esse nome"}, 409

    return {"msg": "Oficina atualizada!"}, 200


def oficinas_buscar_ok(dados):

    if "id" in dados:
        oficina = db.session.get(Oficina, dados["id"])

    elif "nome" in dados:
        oficina = db.session.execute(
            select(Oficina).where(
                Oficina.nome == dados["nome"]
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
