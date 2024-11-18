from config import db
from sqlalchemy import text

def get_reference():
    sql = text("SELECT * FROM reference")
    result = db.session.execute(sql)
    result = result.fetchall()
    refs = []
    for i in result:
        non_none_values = [str(value) for value in i[1:] if value is not None]
        formatted_string = ", ".join(non_none_values)
        refs.append(f"{formatted_string}")

    return refs

def create_reference(ref_dict: dict):
    sql = text("""INSERT INTO reference (citation_key, author, title, journal, year, volume, pages, doi)
                    VALUES (:sitaatin_tunniste, :kirjoittajat, :otsikko, :julkaisu, :vuosi, :julkaisunumero, :sivut, :doi)
               """)
    db.session.execute(sql, {"sitaatin_tunniste":ref_dict["sitaatin_tunniste"], "kirjoittajat":ref_dict["kirjoittajat"], "otsikko":ref_dict["otsikko"], "julkaisu":ref_dict["julkaisu"], "vuosi":ref_dict["vuosi"], "julkaisunumero":ref_dict["julkaisunumero"], "sivut":ref_dict["sivut"], "doi":ref_dict["doi"]})
    db.session.commit()