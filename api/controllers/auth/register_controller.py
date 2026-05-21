from services import register_ok

def register_dados(dados):
    nome = dados["nome"]
    email = dados["email"]
    senha = dados["senha"]
    
    return register_ok(nome, email, senha)