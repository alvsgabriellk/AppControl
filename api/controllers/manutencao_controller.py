from services import manutencao_ok

def manutencao_dados(dados):

    veiculo_id = dados["veiculo_id"]
    oficina_id = dados["oficina_id"]
    tipo_manutencao = dados["tipo_manutencao"]
    valor = float(dados["valor"])
    km_manutencao = float(dados["km_manutencao"])
    garantia_dias = int(dados["garantia_dias"])

    return manutencao_ok(
        veiculo_id, oficina_id,
        tipo_manutencao, valor,
        km_manutencao, garantia_dias
    )
