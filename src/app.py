
from config import app
from flask import redirect, render_template, request, jsonify, flash

from repositories.reference_repository import get_reference, create_reference, delete_all

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

@app.route("/tests/reset", methods=["POST"])
def reset_tests():
    delete_all()
    return "Reset"
