from config import db
from sqlalchemy import text

def get_reference():
    sql = text("SELECT * FROM reference")
    result = db.session.execute(sql)
    result = result.fetchall()
    fields = [
        'author',  # Required
        'title',   # Required
        'journal', # Required
        'year',    # Required
        'volume',  # Optional
        'number',  # Optional
        'pages',   # Optional
        'month',   # Optional
        'note',    # Optional
        'doi',     # Non-standard
        'issn',    # Non-standard
        'zblnumber', # Non-standard
        'eprint',  # Non-standard
    ]

    refs = []
    for row in result:            
        formatted_parts = []
        for field in fields:
            value = getattr(row, field, None)
            print(value)
            print(row, field)
            if value:
                formatted_parts.append(f"{value}")
        
        formatted_string = ", ".join(formatted_parts)
        refs.append(formatted_string)
    
    return refs

def create_reference(ref_dict: dict):
    sql = text("""INSERT INTO reference (citation_key, author, title, journal, year, volume, pages, doi)
                    VALUES (:sitaatin_tunniste, :kirjoittajat, :otsikko, :julkaisu, :vuosi, :julkaisunumero, :sivut, :doi)
               """)
    db.session.execute(sql, {"sitaatin_tunniste":ref_dict["sitaatin_tunniste"], "kirjoittajat":ref_dict["kirjoittajat"], "otsikko":ref_dict["otsikko"], "julkaisu":ref_dict["julkaisu"], "vuosi":ref_dict["vuosi"], "julkaisunumero":ref_dict["julkaisunumero"], "sivut":ref_dict["sivut"], "doi":ref_dict["doi"]})
    db.session.commit()

def delete_all():
    refs = []
    return refs