
from flask import redirect, render_template, request
from config import app

from repositories.reference_repository import get_reference, create_reference, delete_all, get_bib_reference, get_column_names, delete_reference

@app.route("/", methods =["GET", "POST"])
def load_index():
    # reference = get_reference()
    return render_template("index.html")

@app.route("/get_reference", methods =["GET"])
def reference_fetcher():
    """
    Fetches the references and sends them to references.html
    """
    references = get_reference()
    # print("here are the references from app.py",references)
    return render_template("references.html", references=references)

@app.route("/get_columns/<ref_type>", methods =["GET"])
def column_name_fetcher(ref_type):
    """
    Fetches the column names and sends them to index.html
    """
    column_names = get_column_names(ref_type)
    print("here are the columns from app.py", column_names)
    return column_names

@app.route('/create_reference', methods=['POST'])
def create_reference_route():
    """
    Gets form informations and turns it to a dictionary in request.form.to_dict()
    Then gets the reference type and pops it out of the dictionary so its not put into the database.
    Calls create_reference with the dicitonary of the form vlaues and the reference type ex. Book
    """
    ref_dict = request.form.to_dict()
    reference_type = request.form.get("chosen_ref")
    ref_dict.pop("chosen_ref", None)
    # print("here is the ref type",reference_type)
    create_reference(ref_dict, reference_type)
    return redirect('/get_reference')

@app.route("/delete/<citation_key>", methods=["POST"])
def reference_deleter(citation_key):
    """Callaa repositorin 

    Args:
        citation_key (string): uniikki sitaatin avain

    Returns:
        _type_: redirectaa refrence listan
    """
    delete_reference(citation_key)
    return redirect('/get_reference')

@app.route("/tests/reset", methods=["POST"])
def reset_tests():
    delete_all()
    return "Reset"

@app.route("/bib_references", methods=["GET"])
def bib_ref_fetcher():
    bib_refs = get_bib_reference()
    return render_template("bib_ref.html", references = bib_refs)
