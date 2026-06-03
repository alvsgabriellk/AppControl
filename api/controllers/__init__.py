from .auth.register_controller import register_dados
from .veiculo_controller import (
    veiculos_dados, 
    veiculos_lista, 
    veiculos_remover, 
    veiculos_atualizar,
    veiculos_buscar
)
from .auth.login_controller import login_dados
from .veiculo_controller import veiculos_dados
from .oficina_controller import (
    oficina_dados,
    oficinas_lista,
    oficinas_buscar,
    oficinas_remover,
    oficinas_atualizar
)
from .manutencao_controller import (
    manutencao_dados,
    manutencoes_lista,
    manutencoes_remover,
    manutencoes_atualizar,
    manutencoes_buscar
)