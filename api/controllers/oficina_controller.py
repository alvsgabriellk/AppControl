from services import (
    oficina_ok,
    oficinas_lista_ok,
    oficinas_remover_ok,
    oficinas_atualizar_ok,
    oficinas_buscar_ok
)

def oficina_dados(dados):
    nome = dados["nome"]
    telefone = dados["telefone"]
    responsavel = dados["responsavel"]
    endereco = dados["endereco"]
    cidade = dados["cidade"]
    estado = dados["estado"]

    return oficina_ok(
        nome, telefone,
        responsavel, endereco,
        cidade, estado
    )

def oficinas_lista():
    return oficinas_lista_ok()


def oficinas_remover(dados):
    id = dados["id"]

    return oficinas_remover_ok(id)


def oficinas_atualizar(dados):
    return oficinas_atualizar_ok(dados)


def oficinas_buscar(dados):
    return oficinas_buscar_ok(dados)