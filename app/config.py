import os


class Development:
    DEBUG = True
    TESTING = False
    DATABASE_URI='postgresql+psycopg2://postgres:new_password@localhost/mc45'


app_config = {
    'development': Development
}
