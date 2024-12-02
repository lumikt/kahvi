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

            formatted_parts = [f"{getattr(result, field, None)}"
                               for field in fields if getattr(result, field, None)]

            formatted_string = ", ".join(formatted_parts[1:])

            refs.append(formatted_string)

    return refs

def get_column_names(ref_type):
    """
    Get references column names and required or not for index.html form inputs
    returns a list consisting the columns names
    """
    fields = []
    column_query = text("""
        SELECT column_name, is_nullable
        FROM information_schema.columns
        WHERE table_name = :table_name
        ORDER BY ordinal_position
    """)
    column_result = db.session.execute(column_query, {"table_name": ref_type})
    fields = [{"name": row[0], "required": row[1] == "NO"} for row in column_result.fetchall()]

    return fields

def delete_reference(citation_key):
    """Poistaa referenssin

    Args:
        citation_key (string): referenssin uniikki tunniste
    """
    ref_query = text("DELETE FROM reference WHERE citation_key = :key")
    db.session.execute(ref_query, {"key": citation_key})
    db.session.commit()


def get_bib_reference():
    ref_query = text("SELECT citation_key, type FROM reference")
    ref_result = db.session.execute(ref_query).fetchall()

    refs = []

    for ref in ref_result:
        sanis = {}
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

            for field in fields:
                sanis[field] = None

            for field in fields:
                value = getattr(result, field, None)
                if value:
                    sanis[field] = value
                else:
                    del sanis[field]

        refs.append(reference_to_string(sanis,ref.type))

    #nyt sanakirja antaa avaimelle arvon None jos vapaaehtoista kenttää ei ole täytetty
    #sanakirjan käsittely html:ssä ei vielä onnistu kunnolla (tällä hetkellä html toistaa vain yhtä elementtiä)

    return refs

def reference_to_string(ref_dict: dict,ref_type: str = None):
    """
    Takes a reference dictionary and returns it in bibtex format using html formatting.
    Args:
        ref_dict (dict): dictionary containing reference info
        ref_type (string): type of reference being converted
    """
    i = 0
    ref_dict.pop("id")
    citation_key = ref_dict.pop("citation_key")

    string_conversion = f'@{ref_type.upper()}' + "{" +  f'{citation_key}, <br>'
    for key,value in ref_dict.items():
        if i == len(ref_dict)-1:
            string_conversion  +=  f'&nbsp;&nbsp;&nbsp;{key} = "{value}"<br>'
            break
        string_conversion  +=  f'&nbsp;&nbsp;&nbsp;{key} = "{value}",<br>'
        i+= 1

    string_conversion += "&nbsp;}"
    return string_conversion

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

def create_tag(tag_name, ref_id=None):
    """
    Function to create a tag. Create the tag in the tags table in sql.
    If there is a reference id, create an entry in the ref_tags table to link the
    tag to a reference.
    """

    sql_tag = text("""INSERT INTO tags (name)
                      VALUES (:name)
                      RETURNING id
                   """)
    result = db.session.execute(sql_tag, {"name": tag_name })
    tag_id = result.scalar()

    if ref_id:
        sql = text("""INSERT INTO ref_tags (ref_id, tag_id)
                      VALUES (:ref_id, :tag_id)
                   """)
        db.session.execute(sql, {"ref_id": ref_id, "tag_id": tag_id})

def delete_all():
    refs = []
    return refs
