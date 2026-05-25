from flask import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
veic_bp = Blueprint("veic", __name__, url_prefix="/veic")
ofic_bp = Blueprint("ofic", __name__, url_prefix="/ofic")
mant_bp = Blueprint("mant", __name__, url_prefix="/mant")

from .auth import register_routes, login_routes
from routes import veiculo_routes
from routes import oficina_routes
from routes import manutencao_routes