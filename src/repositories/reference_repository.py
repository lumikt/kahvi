from tempfile import TemporaryFile
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

        fields = [column["name"] for column in get_column_names(ref_type.lower())]

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
    table_name = ref_type.lower()
    column_query = text("""
        SELECT column_name, is_nullable
        FROM information_schema.columns
        WHERE table_name = :table_name
        ORDER BY ordinal_position
    """)
    column_result = db.session.execute(column_query, {"table_name": table_name})
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

def get_reference_by_id(citation_key):
    """get ref by 

    Args:
        citation_key (string): ref key

    Returns:
        database query for ref by id
    """
    type_result = get_reference_type_id(citation_key)

    data_query = text(f"SELECT * FROM {type_result} WHERE citation_key = :citation_key")
    result = db.session.execute(data_query, {"citation_key": citation_key}).fetchone()
    return result

def get_reference_type_id(citation_key):
    """gets reference type by id

    Args:
        citation_key (string): ref key

    Returns:
        the ref type
    """
    ref_type_query = text("SELECT type FROM reference WHERE citation_key = :citation_key")
    ref_type = db.session.execute(ref_type_query, {"citation_key": citation_key}).fetchone()[0]
    return ref_type

def edit_reference(old_citation_key, ref_dict, ref_type):
    """Function for editing references
    
    Args:
        vanha viitteen avain, formin sanakirja ja viitteen tyyppi"""
    new_citation_key = ref_dict["citation_key"]

    #katsoo onko citation key päivittynyt. Jos on päivittää reference taulukkoon ja omaan taulukkoon sen
    if new_citation_key != old_citation_key:
        insert_new_key_query = text("""
            INSERT INTO reference (citation_key, type)
            VALUES (:new_citation_key, :type)
        """)
        db.session.execute(insert_new_key_query, {
            "new_citation_key": new_citation_key,
            "type": ref_type
        })

        specific_table_update_query = text(f"""
            UPDATE {ref_type}
            SET citation_key = :new_citation_key
            WHERE citation_key = :old_citation_key
        """)
        db.session.execute(specific_table_update_query, {
            "new_citation_key": new_citation_key,
            "old_citation_key": old_citation_key
        })

        delete_old_key_query = text("""
            DELETE FROM reference
            WHERE citation_key = :old_citation_key
        """)
        db.session.execute(delete_old_key_query, {
            "old_citation_key": old_citation_key
        })

    #hakee kolumnien nimet ref_dictista ja päivittää kentät
    columns = ", ".join([f"{key} = :{key}" for key in ref_dict.keys() if key != "citation_key"])
    specific_table_field_update_query = text(f"""
        UPDATE {ref_type}
        SET {columns}
        WHERE citation_key = :citation_key
    """)
    db.session.execute(specific_table_field_update_query, ref_dict)

    db.session.commit()


def get_bib_reference_from_db():
    ref_query = text("SELECT citation_key, type FROM reference")
    ref_result = db.session.execute(ref_query).fetchall()

    refs = []

    for ref in ref_result:
        sanis = {}
        citation_key, ref_type = ref.citation_key, ref.type
        sanis["ref_type"] = ref.type
        data_query = text(f"SELECT * FROM {ref_type} WHERE citation_key = :citation_key")
        result = db.session.execute(data_query, {"citation_key": citation_key}).fetchone()

        #pitää loweraa case jotta column query toimii
        table_name = ref_type.lower()
        if result:
            column_query = text("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_name = :table_name
                ORDER BY ordinal_position
            """)
            column_result = db.session.execute(column_query, {"table_name": table_name})
            fields = [row[0] for row in column_result.fetchall()]

            for field in fields:
                sanis[field] = None

            for field in fields:
                value = getattr(result, field, None)
                if value:
                    sanis[field] = value
                else:
                    del sanis[field]

        refs.append(sanis)

    #nyt sanakirja antaa avaimelle arvon None jos vapaaehtoista kenttää ei ole täytetty
    #sanakirjan käsittely html:ssä ei vielä onnistu kunnolla (tällä hetkellä html toistaa vain yhtä elementtiä)

    return refs

def get_bib_reference():
    formatted_references = []
    refs = get_bib_reference_from_db()
    for reference in refs:
        formatted_references.append(reference_to_html_string(reference))

    return formatted_references

def reference_to_html_string(ref_dict: dict):
    """
    Takes a reference dictionary and returns it in bibtex format using html formatting.
    Args:
        ref_dict (dict): dictionary containing reference info
    """
    i = 0
    ref_dict.pop("id")
    citation_key = ref_dict.pop("citation_key")
    ref_type = ref_dict.pop("ref_type")
    string_conversion = f'@{ref_type.upper()}' + "{" +  f'{citation_key}, <br>'
    for key,value in ref_dict.items():
        if i == len(ref_dict)-1:
            string_conversion  +=  f'&nbsp;&nbsp;&nbsp;{key} = "{value}"<br>'
            break
        string_conversion  +=  f'&nbsp;&nbsp;&nbsp;{key} = "{value}",<br>'
        i+= 1

    string_conversion += "&nbsp;}"
    return string_conversion

def reference_to_text_string(ref_dict: dict):
    """
    Takes a reference dictionary and returns it in bibtex format text string.
    Args:
        ref_dict (dict): dictionary containing reference info
    """
    i = 0
    ref_dict.pop("id")
    citation_key = ref_dict.pop("citation_key")
    ref_type = ref_dict.pop("ref_type")
    string_conversion = f'@{ref_type.upper()}' + "{" +  f'{citation_key},\n'
    for key,value in ref_dict.items():
        if i == len(ref_dict)-1:
            string_conversion  +=  f'   {key} = "{value}"\n'
            break
        string_conversion  +=  f'   {key} = "{value}",\n'
        i+= 1

    string_conversion += " }\n\n"
    return string_conversion


def get_bibtex_export_file():
    #Käytetään tempfileä jotta ei tiedostoa ei tarvitse tallentaa erikseen minnekään
    tmp = TemporaryFile()
    for reference in get_bib_reference_from_db():
        formatted_reference = reference_to_text_string(reference)

        #Flask.send_file haluaa tiedoston byte muodossa ja kirjoittaa sen sitten oikeaan tiedostomuotoon itse.
        #Ilman tätä tiedoston joutuisi kirjoittamaan johon kansioon ja lähettämään sieltä.
        reference_as_bytes = str.encode(formatted_reference)
        tmp.write(reference_as_bytes)

    #palauttaa kursorin tiedoston alkuun, ilman tätä tmp file näyttää tyhjältä downloadin jälkeen.
    tmp.seek(0)

    return tmp


#%%
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

    #nyt selvittää onko sitaatin avain uniikko vai ei.
    #Pitää tehdä parempi error handling
    existing_reference_query = text("SELECT 1 FROM reference WHERE citation_key = :citation_key")
    existing_reference = db.session.execute(existing_reference_query, {"citation_key": citation_key}).fetchone()

    if existing_reference:
        raise ValueError(f"A reference with citation_key '{citation_key}' already exists.")


    sql_reference = text("""INSERT INTO reference (citation_key, type)
                            VALUES (:citation_key, :type)
                            ON CONFLICT DO NOTHING
                            RETURNING id
                         """)
    result = db.session.execute(sql_reference, {"citation_key": citation_key, "type": reference_type})
    ref_id = result.fetchone()[0]

    columns = ", ".join(ref_dict.keys())
    placeholders = ", ".join([f":{key}" for key in ref_dict.keys()])
    sql = text(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})")

    db.session.execute(sql, ref_dict)
    db.session.commit()

    return ref_id

def create_tag(tag_name, ref_id=None):
    """
    Function to create a tag. Create the tag in the tags table in sql.
    If there is a reference id, create an entry in the ref_tags table to link the
    tag to a reference.
    """
    print("täällä")
    sql_tag = text("""INSERT INTO tags (name)
                      VALUES (:name)
                      RETURNING id
                   """)
    result = db.session.execute(sql_tag, {"name": tag_name })
    tag_id = result.fetchone()[0]
    db.session.commit()

    if ref_id:
        add_tag(ref_id, tag_id)

def add_tag(ref_id, tag_id):
    """
    Function to link an existing tag to a reference via the ref_tags table.
    """
    sql = text("""INSERT INTO ref_tags (ref_id, tag_id)
                      VALUES (:ref_id, :tag_id)
                   """)
    db.session.execute(sql, {"ref_id": ref_id, "tag_id": tag_id})
    db.session.commit()

def get_all_tags():
    """
    Return a list of all tag names in the database
    """
    sql = text("""SELECT DISTINCT id, name
                  FROM tags
               """)
    tags = db.session.execute(sql).fetchall()
    tag_ids = [row[0] for row in tags]
    tag_names = [row[1] for row in tags]
    return tag_ids, tag_names

def get_tags(ref_id):
    """
    Return all tags associated with a reference
    """
    sql = text("""SELECT T.name
                    FROM reference R
                    JOIN ref_tags RT
                        ON R.id=RT.ref_id
                        AND R.id=:ref_id
                    JOIN tags T
                        ON T.id=RT.tag_id
               """)
    
    result = db.session.execute(sql, {"ref_id":ref_id}).fetchall()
    return result

def delete_all():
    refs = []
    return refs
