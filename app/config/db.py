DB_USER = "root"
DB_PASSWORD = "eY7m76S_rP"
DB_HOST = "localhost"
DB_NAME = "hackchange"
DB_PORT = "3306"


def get_db_url():
    return f"mysql+asyncmy://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
