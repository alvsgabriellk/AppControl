from services import login_ok

def login_dados(dados):
    email = dados["email"]
    senha = dados["senha"]

    return login_ok(email, senha)