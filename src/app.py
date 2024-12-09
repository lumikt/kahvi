import json
from flask import redirect, render_template, request, send_file
from config import app
from repositories.reference_repository import (
                                               get_reference,
                                               create_reference,
                                               delete_all,
                                               get_bib_reference,
                                               get_column_names,
                                               delete_reference,
                                               get_reference_by_id,
                                               get_reference_type_id,
                                               edit_reference,
                                               get_bibtex_export_file,
                                               get_tags,
                                               get_search_results,
                                               sync_tags,
                                               get_reference_id
                                            )

@app.route("/", methods =["GET", "POST"])
def load_index():
    return render_template("index.html")

@app.route("/get_reference", methods =["GET"])
def reference_fetcher():
    """
    Fetches the references and sends them to references.html
    """
    references = get_reference()
    return render_template("references.html", references=references)

@app.route("/add_reference", methods=["GET"])
def reference_creator():
    """
    Goes to creating new reference page
    """
    return render_template("add_reference.html")

@app.route("/get_columns/<ref_type>", methods =["GET"])
def column_name_fetcher(ref_type):
    """
    Fetches the column names and sends them to index.html
    """
    ref_type.lower()
    column_names = get_column_names(ref_type)
    return column_names

@app.route('/create_reference', methods=['POST'])
def create_reference_route():
    """
    creates a reference and then adds tags if there are any and also links them to the ref.
    """
    ref_dict = request.form.to_dict()
    reference_type = ref_dict.pop("chosen_ref", None)

    tags = ref_dict.pop("tags", None)
    tags = json.loads(tags) if tags else []

    ref_id = create_reference(ref_dict, reference_type)

    sync_tags(ref_id, tags)

    return redirect('/get_reference')

@app.route("/edit/<citation_key>", methods=["GET", "POST"])
def reference_editer(citation_key):
    """Reitti referenssien editointiin

    Args:
        citation_key (string): refen avain

    Returns:
        jos get niin edit ref htmlän missä voi muokata viitettä. 
        Ja jos post niin redirectaa referenssien listaan
    """
    if request.method == "GET":
        reference = get_reference_by_id(citation_key)
        ref_id = get_reference_id(citation_key)

        tags = json.dumps(get_tags(ref_id))
        ref_type = get_reference_type_id(citation_key)
        columns  = column_name_fetcher(ref_type)

        return render_template("edit_ref.html", tags=tags, ref_id=ref_id, reference=reference, ref_type=ref_type, columns=columns)

    if request.method == "POST":
        reference = get_reference_by_id(citation_key)
        ref_id = get_reference_id(citation_key)
        ref_dict = request.form.to_dict()
        ref_type = get_reference_type_id(citation_key)
        ref_dict.pop("chosen_ref", None)

        tags = json.loads(ref_dict.pop("tags", None))

        edit_reference(citation_key, ref_dict, ref_type, ref_id, tags)

        return redirect('/get_reference')

    #if not get or post return this
    return "Method Not Allowed", 405


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
    return render_template("bib_ref.html", references=bib_refs)


@app.route("/exportBibtex", methods=["GET"])
def bib_ref_exporter():
    bib_refs = get_bibtex_export_file()

    return send_file(bib_refs,mimetype='text',as_attachment=True,download_name="bibtex_strings.bib")

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    search_results = get_search_results(query)

    return render_template("references.html", references=search_results)
