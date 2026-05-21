from flask import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
veic_bp = Blueprint("veic", __name__, url_prefix="/veic")

from .auth import register_routes
