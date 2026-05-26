from services import veiculo_ok, veiculos_lista_ok, veiculos_remover_ok

def veiculos_dados(dados):

    usuario_id = dados["usuario_id"]
    placa = dados["placa"]
    renavan = dados["renavan"]
    marca = dados["marca"]
    modelo = dados["modelo"]
    km_compra = float(dados["km_compra"])
    km_atual = float(dados["km_atual"])

    return veiculo_ok(
        usuario_id, placa, 
        renavan, marca, 
        modelo, km_compra,
        km_atual
    )

def veiculos_lista():
    return veiculos_lista_ok()


def veiculos_remover(dados):
    id = dados["id"]

    return veiculos_remover_ok(id)
    
