import os




class Config:
    SECRET_KEY = "super_secret_key" or os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db" or os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')