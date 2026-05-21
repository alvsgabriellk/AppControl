import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    KEY_API = os.getenv("KEY_API")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

