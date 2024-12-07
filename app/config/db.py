

import os

def get_db_url():
    # if os.environ.get('DEBUG', False):
    # DB_USER =  os.environ.get('USER', 'root')
    # DB_PASSWORD =  os.environ.get('PASSWORD', 'eY7m76S_rP')
    # DB_HOST =  os.environ.get('HOST', 'localhost')
    # DB_PORT = os.environ.get('PORT', '3306')
    # DB_NAME =  os.environ.get('DB', 'hackchange')
    DB_USER = "root"
    DB_PASSWORD = "eY7m76S_rP"
    DB_HOST = "localhost"
    DB_NAME = "hackchange"
    DB_PORT = "3306"
    return f"mysql+asyncmy://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
