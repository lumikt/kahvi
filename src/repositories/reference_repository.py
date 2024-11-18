from config import db
from sqlalchemy import text

def get_reference():
    pass

def create_reference(ref_dict: dict):
    sql = text("""INSERT INTO reference (citation_key, author, title, journal, year, volume, pages, doi)
                    VALUES (:sitaatin_tunniste, :kirjoittajat, :otsikko, :julkaisu, :vuosi, :julkaisunumero, :sivut, :doi)
               """)
    db.session.execute(sql, {"sitaatin_tunniste":ref_dict["sitaatin_tunniste"], "kirjoittajat":ref_dict["kirjoittajat"], "otsikko":ref_dict["otsikko"], "julkaisu":ref_dict["julkaisu"], "vuosi":ref_dict["vuosi"], "julkaisunumero":ref_dict["julkaisunumero"], "sivut":ref_dict["sivut"], "doi":ref_dict["doi"]})
    db.session.commit()