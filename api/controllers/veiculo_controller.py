from services import (
    veiculo_ok, 
    veiculos_lista_ok, 
    veiculos_remover_ok, 
    veiculos_atualizar_ok, 
    veiculos_buscar_ok
)

def veiculos_dados(dados):

    placa = dados["placa"]
    renavan = dados["renavan"]
    marca = dados["marca"]
    modelo = dados["modelo"]
    marca_modelo = dados["marca_modelo"]
    ano_modelo = dados["ano_modelo"]
    cor = dados["cor"]
    km_compra = float(dados["km_compra"])
    km_atual = float(dados["km_atual"])

    return veiculo_ok(
        placa, 
        renavan, marca, 
        modelo, marca_modelo,
        ano_modelo, cor,
        km_compra, km_atual
    )

def veiculos_lista():
    return veiculos_lista_ok()


def veiculos_remover(dados):
    id = dados["id"]

    return veiculos_remover_ok(id)

def veiculos_atualizar(dados):
    return veiculos_atualizar_ok(dados)

def veiculos_buscar(dados):
    return veiculos_buscar_ok(dados)
    
