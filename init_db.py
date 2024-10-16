import os
import sqlite3


db_path = "./PolinasVoice.db"


if not os.path.exists(db_path):
    print("База данных не найдена. Создаю базу данных...")
    conn = sqlite3.connect(db_path)
    conn.close()
    print(f"База данных '{db_path}' создана.")
else:
    print(f"База данных '{db_path}' уже существует.")