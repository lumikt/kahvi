from os import path
from sqlalchemy import text
from config import db, app

def table_exists(name):
    sql_table_existence = text(
    "SELECT EXISTS ("
    "  SELECT 1"
    "  FROM information_schema.tables"
    f" WHERE table_name = '{name}'"
    ")"
    )

    print(f"Checking if table {name} exists")
    print(sql_table_existence)

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]


def setup_db(schema):
    print("Creating tables")
    sql = text(schema)
    db.session.execute(sql)
    db.session.commit()


def load_schema(file_path):
    with open(file_path, "r") as file:
        sql = file.read()
    print(sql)
    return sql


if __name__ == "__main__":
    with app.app_context():
        project_root = path.dirname(path.abspath(__file__))
        schema_file = path.join(project_root, "../schema.sql")
        db_schema = load_schema(schema_file)
        setup_db(db_schema)
