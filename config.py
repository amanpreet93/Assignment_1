import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

class Config(object):
    ENV='development'
    DEBUG=True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Start@1234@127.0.0.1:3306/alchemy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED=True
    

 