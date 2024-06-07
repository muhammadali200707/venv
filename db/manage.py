import os
import psycopg2 as psql
from dotenv import load_dotenv

load_dotenv()


class Database:
    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database=os.getenv('db_name'),
            user=os.getenv('db_user'),
            password=os.getenv('db_password'),
            host=os.getenv('db_host'),
            port=os.getenv("db_port")
        )
        cursor = db.cursor()
        cursor.execute(query)
        data = ['create', 'update', 'delete', 'insert', 'alter']
        if query_type in data:
            db.commit()
            if query_type == 'create':
                return f"created successfully"
            return f"{query_type}ed successfully"
        else:
            return cursor.fetchall()
