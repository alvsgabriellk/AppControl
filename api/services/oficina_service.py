
from database import db, Oficina
from sqlalchemy.exc import IntegrityError

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
