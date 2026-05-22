from flask import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
veic_bp = Blueprint("veic", __name__, url_prefix="/veic")
ofic_bp = Blueprint("ofic", __name__, url_prefix="/ofic")

from .auth import register_routes
from routes import veiculo_routes