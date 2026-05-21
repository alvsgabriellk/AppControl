from flask import Flask
from flask_cors import CORS
from database import db
import os
from config import DesenvolvimentoConfig, ProducaoConfig

app = Flask(__name__)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

