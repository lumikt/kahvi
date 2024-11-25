from config import db, app
from sqlalchemy import text


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

def reset_db():
    # muokataan myöhemmin
    print(f"Clearing contents from table {table_name}")
    sql = text(f"DELETE FROM {table_name}")
    db.session.execute(sql)
    db.session.commit()

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
        schema_file = "../schema.sql"
        schema = load_schema(schema_file)
        setup_db(schema)