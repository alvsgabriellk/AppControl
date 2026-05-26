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