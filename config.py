import os

class Config:
    with open('secret_key') as f:
        SECRET_KEY = f.readline().strip()
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SAMMY_MAIL_SUBJECT_PREFIX = '[Sammy]'
    SAMMY_MAIL_SENDER = 'Sammy Admin <sammy@sammy.com>'
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'postgresql://skeller:holeysmokes@localhost:5432/sammy_db'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
