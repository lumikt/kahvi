
from config import app
from flask import redirect, render_template, request, jsonify, flash

from repositories.reference_repository import get_reference, create_reference

@app.route("/", methods =["GET", "POST"])
def load_index():    
    # reference = get_reference()
    return render_template("index.html")

@app.route("/create_reference", methods = ["POST"])
def reference_creation():
    ref_dict = {}
    ref_dict["kirjoittajat"] = request.form.get("kirjoittajat")
    ref_dict["otsikko"] = request.form.get("otsikko")
    ref_dict["julkaisu"] = request.form.get("julkaisu")
    ref_dict["vuosi"] = request.form.get("vuosi")
    ref_dict["julkaisunumero"] = request.form.get("julkaisunumero")
    ref_dict["sivut"] = request.form.get("sivut")
    ref_dict["doi"] = request.form.get("DOI")
    # return kirjoittajat, otsikko, julkaisu, DOI
    print(ref_dict)
    
    # TODO
    # reference_repository.py funktio joka postaa tietokantaan. 
    create_reference(ref_dict)
    # luo logiikka, tällä hetkellä create_reference funktio pass

    return redirect("/")
