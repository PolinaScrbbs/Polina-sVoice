from dotenv import load_dotenv
import os

class Config():
    def __init__(self):
        load_dotenv()

        print("USER:", os.environ.get("POSTGRES_USER"))
        print("PASSWORD:", os.environ.get("POSTGRES_PASSWORD"))
        print("HOST:", os.environ.get("POSTGRES_HOST", "127.0.0.1"))
        print("PORT:", os.environ.get("POSTGRES_PORT", 5432))
        print("DB:", os.environ.get("POSTGRES_DB"))
    
    USER = os.environ.get("POSTGRES_USER")
    PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    HOST = os.environ.get("POSTGRES_HOST", "127.0.0.1")
    PORT = os.environ.get("POSTGRES_PORT", 5432)
    DB = os.environ.get("POSTGRES_DB")

    ALEMBIC_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = "s;cs-=2d2.'2[pl.#?%@>3';2/35.-23v.'2cp[k-=dod-=o_DAD_+CSC>ASL=-]]"

    MEDIA_FOLDER = 'media'

    