class DefaultConfig(object):
    
    DEBUG = True
    TESTING = False
    
    DB_NAME = "saath.db"

    SECRET_KEY = "sathihelp"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"
    SQLALCHEMY_ECHO = True
