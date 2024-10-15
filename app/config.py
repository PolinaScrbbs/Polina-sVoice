import os

class Config(object):
    USER = os.environ.get("POSTGRES_USER")
    PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    HOST = os.environ.get("POSTGRES_HOST", "127.0.0.1")
    PORT = os.environ.get("POSTGRES_PORT", 5432)
    DB = os.environ.get("POSTGRES_DB")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = "s;cs-=2d2.'2[pl.#?%@>3';2/35.-23v.'2cp[k-=dod-=o_DAD_+CSC>ASL=-]]"
    SQLALCHEMY_TRACK_MODIFICATION = True