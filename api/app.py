from flask import Flask
from database import db

app = Flask(__name__)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

