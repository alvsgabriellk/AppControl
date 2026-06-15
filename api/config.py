import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    KEY_API = os.getenv("KEY_API")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    MAIL_DEFAULT_SENDER = os.getenv("MAIL_USERNAME")


class DesenvolvimentoConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI  = "mysql+pymysql://root:senhaaqui!@localhost:portaaqui/manutencoes"
    JWT_SECRET_KEY = "wnfun3ufn3n83nv8n3vn4jvn"
    '''SQLALCHEMY_DATABASE_URI  = "sqlite:///banco.db"'''
    CORS_ORIGINS = [""]

class ProducaoConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    CORS_ORIGINS = [os.getenv("APP_URL")]