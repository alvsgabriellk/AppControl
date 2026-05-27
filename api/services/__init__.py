from .auth.register_service import register_ok
from .auth.email_service import enviar_confirmacao, enviar_recuperacao

from .veiculo_service import (
    veiculo_ok, 
    veiculos_lista_ok, 
    veiculos_remover_ok, 
    veiculos_atualizar_ok,
    veiculos_buscar_ok
)
from .auth.login_service import login_ok
from .veiculo_service import veiculo_ok
from .oficina_service import (
    oficina_ok,
    oficinas_buscar_ok,
    oficinas_lista_ok,
    oficinas_atualizar_ok,
    oficinas_remover_ok
)
from .manutencao_service import (
    manutencao_ok,
    manutencoes_lista_ok,
    manutencoes_remover_ok,
    manutencoes_buscar_ok,
    manutencoes_atualizar_ok
)
