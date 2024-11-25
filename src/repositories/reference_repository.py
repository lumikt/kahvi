from sqlalchemy import text
from config import db

def get_reference():
    """
    First fetches citaions key and its reference type from reference table.
    Then goes through the results one by one and making a data query from the reference table.
    WIth this dataquery we fetch the reference with its citation key.
    Then we fetch its column names so we can properly format the ref.
    After formating adds it into the refs list and returns it after the loop
    """
    ref_query = text("SELECT citation_key, type FROM reference")
    ref_result = db.session.execute(ref_query).fetchall()

    refs = []

    for ref in ref_result:
        citation_key, ref_type = ref.citation_key, ref.type

        data_query = text(f"SELECT * FROM {ref_type} WHERE citation_key = :citation_key")
        result = db.session.execute(data_query, {"citation_key": citation_key}).fetchone()

        if result:
            column_query = text("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_name = :table_name
                ORDER BY ordinal_position
            """)
            column_result = db.session.execute(column_query, {"table_name": ref_type})
            fields = [row[0] for row in column_result.fetchall()]

            formatted_parts = [f"{getattr(result, field, None)}" for field in fields if getattr(result, field, None)] # pylint: disable=line-too-long

            formatted_string = ", ".join(formatted_parts[2:])

            refs.append(formatted_string)

    return refs

def get_bib_reference():
    ref_query = text("SELECT citation_key, type FROM reference")
    ref_result = db.session.execute(ref_query).fetchall()

    refs = []

    for ref in ref_result:
        citation_key, ref_type = ref.citation_key, ref.type

        data_query = text(f"SELECT * FROM {ref_type} WHERE citation_key = :citation_key")
        result = db.session.execute(data_query, {"citation_key": citation_key}).fetchone()

        if result:
            column_query = text("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_name = :table_name
                ORDER BY ordinal_position
            """)
            column_result = db.session.execute(column_query, {"table_name": ref_type})
            fields = [row[0] for row in column_result.fetchall()]

            formatted_parts = [f"{getattr(result, field, None)}" for field in fields if getattr(result, field, None)]

            formatted_string = f"@{ref_type}"
            formatted_string += "{"
            formatted_string += f"{formatted_parts[1]}, \n"
                                              
            for i in formatted_parts[2:]:
                formatted_string = "\n".join(f"{ i },")

            refs.append(formatted_string)

    return refs



def create_reference(ref_dict: dict, table_name: str):
    """
    Function to create a reference. 
    First we get the citation key and the type of the reference and insert it into reference table.
    Then we get the columns and placeholders from the ref_dict to get the correct style to insert
    into table_name called table for example Article table. Then insert that reference into the 
    table where it belongs.
    """
    citation_key = ref_dict.get("citation_key")
    reference_type = table_name

    sql_reference = text("""INSERT INTO reference (citation_key, type)
                            VALUES (:citation_key, :type)
                            ON CONFLICT DO NOTHING
                         """)
    db.session.execute(sql_reference, {"citation_key": citation_key, "type": reference_type})

    columns = ", ".join(ref_dict.keys())
    placeholders = ", ".join([f":{key}" for key in ref_dict.keys()])
    sql = text(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})")

    db.session.execute(sql, ref_dict)
    db.session.commit()

def delete_all():
    refs = []
    return refs
