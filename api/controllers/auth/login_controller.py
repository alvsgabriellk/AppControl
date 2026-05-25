from services import login_ok

def login_dados(dados):
    nome = dados["nome"]
    email = dados["email"]
    senha = dados["senha"]

    return login_ok(nome, email, senha)