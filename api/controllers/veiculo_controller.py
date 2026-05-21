from services import veiculo_ok

def veiculos_dados(dados):

    usuario_id = dados("usuario_id")
    placa = dados("placa")
    renavan = dados("renavan")
    marca = dados("marca")
    modelo = dados("modelo")
    km_compra = float(dados("km_compra"))
    km_atual = float(dados("km_atual"))

    return veiculo_ok(
        usuario_id, placa, 
        renavan, marca, 
        modelo, km_compra,
        km_atual
    )
    
