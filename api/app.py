from flask import Flask
from flask_cors import CORS
from database import db
import os
from routes import auth_bp, veic_bp
from config import DesenvolvimentoConfig, ProducaoConfig

app = Flask(__name__)

ENV = os.getenv("ENV", "local")
if ENV == "production":
    app.config.from_object(ProducaoConfig)
else:
    app.config.from_object(DesenvolvimentoConfig)

CORS(app, origins=app.config["CORS_ORIGINS"])

db.init_app(app)

app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=app.config.get("DEBUG"))

