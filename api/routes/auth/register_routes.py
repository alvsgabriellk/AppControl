from flask import request, jsonify
from database import db, Usuario
from routes import auth_bp
from controllers import register_dados
