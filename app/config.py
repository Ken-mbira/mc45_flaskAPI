import os


class Development:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://kenmbira:1234@localhost/mc45'


app_config = {
    'development': Development
}
